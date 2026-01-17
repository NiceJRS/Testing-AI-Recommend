from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        file = QFile("ui/home_page.ui")
        file.open(QFile.ReadOnly)

        self.ui = loader.load(file, self)
        self.setLayout(self.ui.layout())
        file.close()
