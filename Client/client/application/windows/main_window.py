from typing import Optional

from PySide6.QtWidgets import QApplication, QGridLayout, QWidget

from ..widgets import FramelessWidget
from ..widgets import Grid


class MainWindow(FramelessWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.grid_enemy = Grid(self)
        self.grid_ally = Grid(self)
        
        self.setWindowTitle("Battleships")

        self.init_layout()
        self.init_widget()

    def init_layout(self):
        QGridLayout(self)

    def init_widget(self):
        self.layout().addWidget(self.grid_ally, 2, 1)
        self.layout().addWidget(self.grid_enemy, 2, 2)
