from PySide6.QtWidgets import QApplication, QWidget
from .windows import MainWindow, LoginWindow

class App(QApplication):
    def __init__(self, arg__1: list):
        super().__init__(arg__1)
        # self._window = MainWindow()
        self._window = LoginWindow()
        self._window.show()

