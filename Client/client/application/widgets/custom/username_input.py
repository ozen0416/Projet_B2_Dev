from typing import Optional

from PySide6.QtWidgets import QHBoxLayout, QWidget, QLineEdit 


class UsernameInput(QLineEdit):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.editingFinished.connect(self.feur)

        self.init_layout()

    def init_layout(self):
        QHBoxLayout(self)

    def feur(self):
        print(self.displayText())
