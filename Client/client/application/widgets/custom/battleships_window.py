from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal


class BattleshipWindow(QWidget):
    switch_window = Signal(str, str)

    def receive_message(self, data: dict):
        pass
