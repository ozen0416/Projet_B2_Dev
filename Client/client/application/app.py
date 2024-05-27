from PySide6.QtWidgets import QApplication
from .windows import GameWindow, HomeWindow

class App(QApplication):
    def __init__(self, arg__1: list):
        super().__init__(arg__1)
        self._window = GameWindow()
        #self._window = HomeWindow()
        self._window.show()

