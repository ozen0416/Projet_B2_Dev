from __future__ import annotations
from typing import Optional

from PySide6.QtGui import QDrag
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QMimeData, Signal

from .grid_cell import GridCell
from ....tools import GridCellState


class ShipWidget(QWidget):
    """
    Ship displayed om the right of the grid to be place.
    This Ship is not on the map
    """
    def __init__(self, size: int, parent: Optional[DisplayShip]):
        super().__init__(parent)
        self._parent = parent
        self._size = size

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        for i in range(self._size):
            ship_cell = GridCell(0, i, GridCellState.SHIP, self)
            self.layout().setSpacing(0)
            self.layout().addWidget(ship_cell)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_drag(event.pos())

    def start_drag(self, start_pos):
        if self._parent.count == 0:
            return
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(str(self._size))
        drag.setMimeData(mime_data)
        drag.setHotSpot(start_pos)
        drag.exec_(Qt.MoveAction)


class DisplayShip(QWidget):
    """
    A Ship and a label displayed in the GUI to keep track of the count of ship left to be placed.
    This ship is not part of the map.
    """

    def __init__(self, count: int, size: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._size = size
        self.count = count
        self.label = QLabel(str(count), self)
        self.ship_widget = ShipWidget(size, self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)
        self.layout().setContentsMargins(100, 10, 10, 10)

    def init_widgets(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.ship_widget)

    def use_ship(self, size):
        print(f"SIGNAL FOR SIZE: {size}")
        if size != self._size:
            return
        if self.count == 0:
            return

        self.count -= 1
        self.label.setText(str(self.count))


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
            count = 2 if i == 3 else 1
            ship = DisplayShip(count, i, self)
            self.layout().addWidget(ship)
            self.ships.append(ship)

