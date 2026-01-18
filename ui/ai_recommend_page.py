from ai_engine import calculate_risk_score, calculate_test_ratio
from datetime import datetime
import logging
from app_state import app_context
from config_loader import load_countries, load_impacted_areas
from excel_exporter import export_ai_recommend_excel
from datetime import datetime
from filter_utils import filter_rows
from service_aggregation import aggregate_service_rows
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QMessageBox,
    QCheckBox,
    QFileDialog,
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt, QMargins
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCharts import QChart, QChartView, QPieSeries

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class AIRecommendPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # ---------- Load UI ----------
        loader = QUiLoader()
        ui_file = QFile("ui/ai_recommend_page.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setLayout(self.ui.layout())

        # =================================================
        # LEFT SIDE : CONFIGURATION (Input)
        # =================================================

        # Title
        self.ui.label.setText("1. CONFIGURATION (Input)")

        # Change Type
        self.ui.groupBox.setTitle("Change Type")
        self.ui.radioButton.setText("Minor")
        self.ui.radioButton_2.setText("Major")
        self.ui.radioButton.setChecked(True)

        # Requirement Type
        self.ui.groupBox_2.setTitle("Requirement Type")
        self.ui.radioButton_3.setText("Common")
        self.ui.radioButton_4.setText("Local")
        self.ui.radioButton_4.setChecked(True)

        # Select Country
        self.ui.groupBox_7.setTitle("Select Country")

        # Impacted Area
        self.ui.groupBox_3.setTitle("Impacted Area")

        self.countries = load_countries()
        self.impacted_area_options = load_impacted_areas()
        self.country_codes = [
            country.get("code", "").upper() for country in self.countries if country.get("code")
        ]
        self._populate_country_combo()
        self._populate_impacted_areas()

        # =================================================
        # RIGHT SIDE : AI ANALYSIS RESULT (Output)
        # =================================================

        # Section title
        self.ui.label_5.setText("2. AI ANALYSIS RESULT (Output)")

        # Top status cards (frames)
        self._fill_frame(self.ui.frame_2, "Vehicle Req:\nYES")

        # Recommended Ratio
        self.ui.groupBox_4.setTitle("Recommended Ratio")
        self.ui.label_6.setText("Manual: 60%\nAuto: 40%")
        self.setup_recommended_ratio_chart()

        # Top 3 High-Risk Scenarios
        self.ui.groupBox_5.setTitle("⚠️ Top 3 High-Risk Scenarios")
        self.ui.label_7.setText("1. Payment Gateway (Local) – 85%")
        self.ui.label_8.setText("2. Login Module (GMS) – 60%")
        self.ui.label_9.setText("3. User Profile Sync – 45%")

        # User Adjustment
        self.ui.groupBox_6.setTitle("User Adjustment")
        self.ui.horizontalSlider_2.setMinimum(0)
        self.ui.horizontalSlider_2.setMaximum(100)
        self.ui.horizontalSlider_2.setValue(0)
        self.ui.horizontalSlider_2.setEnabled(False)
        self.ui.label_10.setText("AI Risk Level: Low Risk (0%)")

        # Export Button
        self.ui.pushButton.setText("Export Test Case (.xlsx)")
        self.ui.pushButton.clicked.connect(self.on_export_clicked)

        # Generate Recommendation
        self.ui.pushButton_2.clicked.connect(self.generate_recommendation)

    # =================================================
    # Helper / Placeholder Methods
    # =================================================

    def _fill_frame(self, frame, text: str):
        """Put centered text into a QFrame (status card placeholder)."""
        layout = QVBoxLayout(frame)
        label = QLabel(text)
        label.setStyleSheet("color: white; font-weight: 700; font-size: 14px;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    def setup_recommended_ratio_chart(self):
        """Replace the text label with a donut chart showing manual vs auto."""
        self.ui.label_6.hide()

        self.ratio_chart = QChart()
        self.ratio_chart.setBackgroundVisible(False)
        self.ratio_chart.setMargins(QMargins(0, 0, 0, 0))
        self.ratio_chart.setContentsMargins(0, 0, 0, 0)
        self.ratio_chart.setBackgroundBrush(Qt.transparent)
        self.ratio_chart.setAnimationOptions(QChart.SeriesAnimations)
        legend = self.ratio_chart.legend()
        legend.setVisible(True)
        legend.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        legend.setFont(QFont("Segoe UI", 10))
        legend.setLabelColor(QColor("#4a4a4a"))

        self.ratio_chart_view = QChartView(self.ratio_chart)
        self.ratio_chart_view.setRenderHint(QPainter.Antialiasing)
        self.ratio_chart_view.setStyleSheet("background-color: transparent;")

        self.manual_ratio_label = QLabel("Manual: 60%")
        self.manual_ratio_label.setStyleSheet("color: #2a2a2a; font-weight: 600;")
        self.auto_ratio_label = QLabel("Automation: 40%")
        self.auto_ratio_label.setStyleSheet("color: #2a2a2a; font-weight: 600;")

        container = QVBoxLayout()
        container.setContentsMargins(0, 0, 0, 0)
        container.addWidget(self.ratio_chart_view)
        container.addWidget(self.manual_ratio_label)
        container.addWidget(self.auto_ratio_label)
        self.ui.groupBox_4.setLayout(container)
        self.update_ratio_chart(60, 40)

    def _populate_country_combo(self):
        self.ui.comboBox.clear()
        for country in self.countries:
            code = country.get("code", "")
            if code:
                label = f"{country['name']} ({code})"
            else:
                label = country["name"]
            self.ui.comboBox.addItem(label, code)

    def _populate_impacted_areas(self):
        layout = self.ui.groupBox_3.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.impacted_area_checkboxes = []
        for area in self.impacted_area_options:
            checkbox = QCheckBox(area)
            layout.addWidget(checkbox)
            self.impacted_area_checkboxes.append(checkbox)

    def update_ratio_chart(self, manual_percent: float, auto_percent: float):
        self.ratio_chart.removeAllSeries()
        series = QPieSeries()
        manual_slice = series.append(f"Manual {int(manual_percent)}%", manual_percent)
        auto_slice = series.append(f"Auto {int(auto_percent)}%", auto_percent)
        manual_slice.setBrush(QColor("#d32f2f"))
        manual_slice.setLabelVisible(True)
        auto_slice.setBrush(QColor("#bdbdbd"))
        auto_slice.setLabelVisible(True)
        series.setHoleSize(0.6)
        series.setPieSize(0.9)
        self.ratio_chart.addSeries(series)
        self.ratio_chart.createDefaultAxes()

    def _selected_impacted_areas(self) -> list[str]:
        return [cb.text() for cb in getattr(self, "impacted_area_checkboxes", []) if cb.isChecked()]


    def _resolve_platform_from_impacted_areas(self, rules: dict) -> str:
        mapping = rules.get("impacted_area_platform", {})
        priority = {"Both": 3, "Mobile": 2, "Web": 2, "Unknown": 1}
        best_platform = "Unknown"
        best_score = 0
        for area in self._selected_impacted_areas():
            platform = mapping.get(area, "Unknown")
            score = priority.get(platform, 1)
            if score > best_score:
                best_score = score
                best_platform = platform
        return best_platform

    def on_export_clicked(self):
        aggregated_rows = app_context.get("aggregated_rows", [])
        row_risk_scores = app_context.get("row_risk_scores", [])
        ratio_summary = app_context.get("ratio_summary", "")

        if not aggregated_rows:
            QMessageBox.information(
                self,
                "Export Test Case",
                "Load test case data before exporting.",
            )
            return

        if not row_risk_scores or not ratio_summary:
            QMessageBox.warning(
                self,
                "Export Test Case",
                "Please generate AI recommendation before exporting.",
            )
            return

        default_name = datetime.now().strftime(
            "AI_Recommend_Test_Case_%Y%m%d_%H%M.xlsx"
        )
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Test Case",
            default_name,
            "Excel Files (*.xlsx)",
        )
        if not path:
            return

        try:
            export_ai_recommend_excel(
                aggregated_rows, row_risk_scores, ratio_summary, path
            )
            QMessageBox.information(self, "Export Test Case", "Exported successfully.")
        except Exception as exc:
            QMessageBox.critical(self, "Export Failed", str(exc))


    def generate_recommendation(self):
        groups = app_context.get("service_groups", [])
        if not groups:
            QMessageBox.information(
                self,
                "AI Recommendation",
                "Import test cases before generating the recommendation.",
            )
            return

        raw_rows = app_context.get("raw_rows", [])
        if not raw_rows:
            QMessageBox.information(
                self,
                "AI Recommendation",
                "Import test cases before generating the recommendation.",
            )
            return

        requirement_type = "Local" if self.ui.radioButton_4.isChecked() else "Common"
        country_code = self.ui.comboBox.currentData() or ""
        filtered_rows = filter_rows(
            raw_rows, requirement_type, country_code, self.country_codes
        )
        if not filtered_rows:
            QMessageBox.information(
                self,
                "AI Recommendation",
                "No test cases match the selected filters.",
            )
            return

        rows_table, aggregated_rows = aggregate_service_rows(filtered_rows)
        service_groups = {}
        for row in filtered_rows:
            service_groups.setdefault(row.get("service", "Unknown"), []).append(row)
        app_context["service_groups"] = service_groups
        app_context["filtered_groups"] = aggregated_rows

        try:
            user_inputs = {
                "change_type": "Major" if self.ui.radioButton_2.isChecked() else "Minor",
                "impacted_areas": self._selected_impacted_areas(),
            }

            # Risk calculation (service level, independent from ratio)
            impacted_areas = self._selected_impacted_areas()
            scored_rows = calculate_risk_score(
                aggregated_rows,
                user_inputs["change_type"],
                impacted_areas,
            )
            # Ratio calculation (service level, independent from risk)
            ratio_result = calculate_test_ratio(aggregated_rows)
     

            app_context["filtered_rows"] = filtered_rows
            app_context["aggregated_rows"] = aggregated_rows
            app_context["row_risk_scores"] = [row.get("risk_score", 0) for row in scored_rows]
            app_context["ratio_result"] = ratio_result
            app_context["ratio_summary"] = (
                f"Manual {ratio_result['manual_percent']}% / "
                f"Auto {ratio_result['auto_percent']}%"
            )
            app_context["ai_results"] = []
            if scored_rows:
                avg_risk = int(
                    sum(row.get("risk_score", 0) for row in scored_rows) / len(scored_rows)
                )
            else:
                avg_risk = 0
            app_context["last_run"] = {
                "average_risk": avg_risk,
                "manual_percent": ratio_result.get("manual_percent", 0),
                "auto_percent": ratio_result.get("auto_percent", 0),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }

            self._update_ui_with_results(scored_rows, ratio_result)
        except Exception as exc:
            logging.error("Error generating AI recommendation: %s", exc, exc_info=True)
            QMessageBox.critical(self, "AI Recommend Failed", str(exc))

    
    
    def summarize_risk(self, scored_rows: list[dict]) -> dict:
        if not scored_rows:
            return {
                "average_risk": 0,
                "max_risk": 0,
                "risk_level": "Low",
            }

        scores = [row.get("risk_score", 0) for row in scored_rows]
        avg = int(sum(scores) / len(scores))
        max_risk = max(scores)

        if avg >= 70:
            level = "High"
        elif avg >= 40:
            level = "Medium"
        else:
            level = "Low"

        return {
            "average_risk": avg,
            "max_risk": max_risk,
            "risk_level": level,
        }

    def _update_ui_with_results(self, scored_rows: list, ratio_result: dict):
        if scored_rows:
            avg_risk = int(
                sum(row.get("risk_score", 0) for row in scored_rows) / len(scored_rows)
            )
        else:
            avg_risk = 0
        self.ui.label_5.setText(f"AI Risk Score: {avg_risk}%")
        self.update_ratio_chart(
            ratio_result.get("manual_percent", 0),
            ratio_result.get("auto_percent", 0),
        )
        self.manual_ratio_label.setText(
            f"Manual: {ratio_result.get('manual_percent', 0)}%"
        )
        self.auto_ratio_label.setText(
            f"Automation: {ratio_result.get('auto_percent', 0)}%"
        )
        risk_level = "Low Risk"
        if avg_risk >= 70:
            risk_level = "High Risk"
        elif avg_risk >= 40:
            risk_level = "Medium Risk"
        self.ui.horizontalSlider_2.setValue(int(avg_risk))
        self.ui.label_10.setText(f"AI Risk Level: {risk_level} ({avg_risk}%)")

        ranked_rows = sorted(
            scored_rows,
            key=lambda row: row.get("risk_score", 0),
            reverse=True,
        )
        for idx, label in enumerate((self.ui.label_7, self.ui.label_8, self.ui.label_9)):
            if idx < len(ranked_rows):
                row = ranked_rows[idx]
                label.setText(
                    f"{idx+1}. {row.get('service', 'Unknown')} – Risk {row.get('risk_score', 0)}%"
                )
            else:
                label.setText(f"{idx+1}. —")
