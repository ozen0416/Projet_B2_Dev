from typing import Optional

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

from .grid_cell import GridCell
from ....tools import GridCellState


class DisplayShip(QWidget):
    """
    Ship displayed in the GUI.
    This ship is not part of the map.
    """

    def __init__(self, size: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._size = size
        self.label = QLabel(self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)
        self.layout().setContentsMargins(100, 10, 10, 10)

    def init_widgets(self):
        self.layout().addWidget(self.label)
        for i in range(self._size):
            ship_cell = GridCell(0, i, GridCellState.SHIP, self)
            self.layout().setSpacing(0)
            self.layout().addWidget(ship_cell)


class DisplayShipContainer(QWidget):
    """
    Container of multiple DisplayShips
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ships = []

        self.button = QPushButton("CONFIRM", self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.layout().addWidget(self.button)
        for i in range(5, 1, -1):
            ship = DisplayShip(i, self)
            self.layout().addWidget(ship)

