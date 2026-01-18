from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from app_state import app_context


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        file = QFile("ui/home_page.ui")
        file.open(QFile.ReadOnly)

        self.ui = loader.load(file, self)
        self.setLayout(self.ui.layout())
        file.close()

        self._label_overall_risk = self.ui.findChild(QLabel, "labelOverallRisk")
        self._label_risk_level = self.ui.findChild(QLabel, "labelRiskLevel")
        self._label_recent_task = self.ui.findChild(QLabel, "labelRecentTask")
        self._label_ai_insight = self.ui.findChild(QLabel, "labelAIInsight")

        self.refresh_home()

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh_home()

    def refresh_home(self):
        last_run = app_context.get("last_run")
        if not last_run:
            self._set_label_text(self._label_overall_risk, "No data yet")
            self._set_label_text(self._label_risk_level, "")
            self._set_label_text(self._label_recent_task, "No recent AI run.")
            self._set_label_text(
                self._label_ai_insight,
                "Generate AI Recommendation to see insights here.",
            )
            return

        average_risk = int(last_run.get("average_risk", 0))
        manual_percent = int(last_run.get("manual_percent", 0))
        auto_percent = int(last_run.get("auto_percent", 0))

        if average_risk >= 70:
            risk_level = "High"
            insight = (
                "This change carries a high overall risk, driven by security "
                "sensitivity and vehicle-related actions. Manual testing is "
                "strongly recommended."
            )
        elif average_risk >= 40:
            risk_level = "Medium"
            insight = (
                "The overall risk is moderate. A balanced mix of manual and "
                "automated testing is recommended."
            )
        else:
            risk_level = "Low"
            insight = (
                "This change has a low risk profile and is suitable for "
                "automation-heavy testing."
            )

        self._set_label_text(self._label_overall_risk, f"{average_risk}%")
        self._set_label_text(self._label_risk_level, risk_level)
        self._set_label_text(
            self._label_recent_task,
            f"Manual {manual_percent}% / Auto {auto_percent}%",
        )
        self._set_label_text(self._label_ai_insight, insight)

    @staticmethod
    def _set_label_text(label: QLabel, text: str):
        if label is not None:
            label.setText(text)
