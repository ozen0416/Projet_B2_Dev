from typing import Optional

from PySide6.QtWidgets import QApplication, QGridLayout, QWidget

from ..widgets import FramelessWidget
from ..widgets import GridContainer


class GameWindow(QWidget):
    """
    Window of the game.
    Displays players' grids, a chat and the history of past moves
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.grid_enemy = GridContainer("Enemy", self)
        self.grid_ally = GridContainer("Ally", self)
        
        self.setWindowTitle("Battleships")

        self.init_layout()
        self.init_widget()

    def init_layout(self):
        QGridLayout(self)

    def init_widget(self):
        self.layout().addWidget(self.grid_ally, 1, 2)
        self.layout().addWidget(self.grid_enemy, 2, 2)