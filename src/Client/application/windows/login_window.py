from typing import Optional

from PySide6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton

from ..widgets import FramelessWidget

class LoginWindow(FramelessWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.input = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.setWindowTitle("Battleships Login")

        self.init_layout()
        self.init_widget()

    def init_layout(self):
        QVBoxLayout(self)

    def init_widget(self):
        self.layout().addWidget(self.input)
        self.layout().addWidget(self.button)
