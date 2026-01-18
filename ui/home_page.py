from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QProgressBar

from app_state import app_context


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        file = QFile("ui/home_page.ui")
        file.open(QFile.ReadOnly)

        self.ui = loader.load(file, self)
        file.close()

        self._label_overall_risk = self.ui.findChild(QLabel, "label")
        self._label_risk_level = self.ui.findChild(QLabel, "labelRiskLevel")
        self._label_automation = self.ui.findChild(QLabel, "label_5")
        self._label_requirement = self.ui.findChild(QLabel, "label_6")
        self._label_ai_insight = self.ui.findChild(QLabel, "cardAutomationValue")
        self._progress_bar = self.ui.findChild(QProgressBar, "progressBar")

        print("HOME app_context id =", id(app_context))
        print("HOME last_run =", app_context.get("last_run"))
    
        self.refresh_home()

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh_home()

    def refresh_home(self):
        last_run = app_context.get("last_run")
        if not last_run:
            self._set_label_text(self._label_overall_risk, "No data yet")
            self._set_label_text(self._label_risk_level, "")
            self._set_label_text(self._label_automation, "No recent AI run.")
            self._set_label_text(
                self._label_ai_insight,
                "Generate AI Recommendation to see insights here.",
            )
            return
        
        print("Refresh HOME app_context id =", id(app_context))
        print("2HOME app_context id =", id(app_context))
        print("2HOME last_run =", app_context.get("last_run"))

        average_risk = int(last_run.get("average_risk", 0))
        manual_percent = int(last_run.get("manual_percent", 0))
        auto_percent = int(last_run.get("auto_percent", 0))
        country = last_run.get("country")
        requirement = last_run.get("requirement")

        if average_risk >= 70:
            risk_level = "High"
            insight = (
                "This change carries a high overall risk, driven by security "
                "sensitivity and vehicle-related actions. Manual testing is "
                "strongly recommended."
            )
            color = "#d32f2f" 
        elif average_risk >= 40:
            risk_level = "Medium"
            insight = (
                "The overall risk is moderate. A balanced mix of manual and "
                "automated testing is recommended."
            )
            color = "#f9a825" 
        else:
            risk_level = "Low"
            insight = (
                "This change has a low risk profile and is suitable for "
                "automation-heavy testing."
            )
            color = "#388e3c" 

        self._set_label_text(self._label_overall_risk, f"{average_risk}%")
        self._set_label_text(self._label_risk_level, risk_level)
        self._set_label_text(
            self._label_automation,
            f"Manual {manual_percent}% / Auto {auto_percent}%",
        )
        self._set_label_text(
            self._label_requirement,
            requirement,
        )

        self._label_risk_level.setStyleSheet(
            f"font-weight: bold; color: {color};"
        )
        
        self._set_label_text(self._label_ai_insight, insight)
        if self._progress_bar:
            self._progress_bar.setValue(average_risk)

        self.update()
        QApplication.processEvents()

    @staticmethod
    def _set_label_text(label: QLabel, text: str):
        if label is not None:
            label.setText(text)
