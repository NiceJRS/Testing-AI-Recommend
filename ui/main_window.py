from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QStackedWidget, QSizePolicy
)
from PySide6.QtCore import Qt

from ui.home_page import HomePage
from ui.testcase_page import TestCasePage
from ui.ai_recommend_page import AIRecommendPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testing AI Recommend")

        # DPI-safe: allow resize while keeping a minimum size
        self.setMinimumSize(1200, 720)

        # ---- Central ----
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # ---- Sidebar ----
        sidebar = QWidget()
        sidebar.setFixedWidth(220)
        sidebar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sidebar.setStyleSheet("background-color: #2b2b2b;")

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)

        title = QLabel("🤖  Testing AI\nRecommend")
        title.setStyleSheet("""
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 16px;
        """)
        sidebar_layout.addWidget(title)

        self.btn_home = QPushButton("🏠  Home")
        self.btn_testcase = QPushButton("📋  Test Case")
        self.btn_ai = QPushButton("🚀  AI Recommend")

        for btn in (self.btn_home, self.btn_testcase, self.btn_ai):
            btn.setMinimumHeight(44)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    color: white;
                    text-align: left;
                    padding-left: 16px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #3c3c3c;
                }
                QPushButton:checked {
                    background-color: #d32f2f;
                }
            """)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        # ---- Pages ----
        self.stack = QStackedWidget()
        self.page_home = HomePage()
        self.page_testcase = TestCasePage()
        self.page_ai = AIRecommendPage()

        self.stack.addWidget(self.page_home)
        self.stack.addWidget(self.page_testcase)
        self.stack.addWidget(self.page_ai)

        # ---- Layout Combine ----
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)

        # ---- Events ----
        self.btn_home.clicked.connect(lambda: self.switch_page(0))
        self.btn_testcase.clicked.connect(lambda: self.switch_page(1))
        self.btn_ai.clicked.connect(lambda: self.switch_page(2))

        self.page_ai.ai_generated.connect(self.on_ai_generated)

        self.switch_page(0)

    def on_ai_generated(self):
        self.page_home.refresh_home()

    def switch_page(self, index: int):
        self.stack.setCurrentIndex(index)
        self.btn_home.setChecked(index == 0)
        self.btn_testcase.setChecked(index == 1)
        self.btn_ai.setChecked(index == 2)
