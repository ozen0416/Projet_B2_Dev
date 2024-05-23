from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton
from typing import Optional

class Grid(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.buttons = []
        
        self.init_layout()
        self.init_grid_button()

    def init_layout(self):
        QGridLayout(self)

    def init_grid_button(self):
        for i in range(5):
            for j in range(5):
                button = QPushButton(str(i)+str(j))
                self.layout().addWidget(button, i, j)
                self.buttons.append(button)
