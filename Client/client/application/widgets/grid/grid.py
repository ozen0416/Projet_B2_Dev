from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout 
from typing import Optional

from ....tools import GridCellState
from .grid_cell import GridCell


class Grid(QWidget):
    """
    A grid of multiple GridCell
    Instantiate all GridCell as WATER
    """

    def __init__(self, size: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.buttons = []
        self._size = size

        self.init_layout()
        self.init_grid_button()

    def init_layout(self):
        QGridLayout(self)
        self.layout().setSpacing(0)

    def init_grid_button(self):
        """
        Initiate grid of buttons
        """
        for i in range(self._size):
            for j in range(self._size):
                button = GridCell(j, i, GridCellState.WATER, self)
                button.setFixedSize(40, 40)
                self.layout().addWidget(button, j, i)
                self.layout().setContentsMargins(0, 0, 0, 0)
                self.buttons.append(button)


class GridContainer(QWidget):
    """
    Container of the grid and its title
    The title is either "Ally" or "Enemy"
    """

    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        self.label = QLabel(title, self)
        self.grid = Grid(10, self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def init_widgets(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.grid)

