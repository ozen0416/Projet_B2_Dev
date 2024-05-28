from PySide6.QtWidgets import QApplication
from .windows import GameWindow, HomeWindow

class App(QApplication):
    def __init__(self, arg__1: list):
        super().__init__(arg__1)
        #self._window = GameWindow()
        with open("./styles/style.qss", 'r', encoding="utf-8") as theme:
            self.setStyleSheet(theme.read())
        self._window = HomeWindow()
        self._window.show()

    @property
    def user(self):
        return "ozen"
