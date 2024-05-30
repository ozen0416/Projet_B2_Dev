from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QStyleOption, QStyle, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

from ....tools import GridCellState


class GridCell(QWidget):
    """
    Single Cell meant to be part of a Grid

    The Cell can have the state WATER or the state SHIP
    """

    def __init__(self, x: int, y: int, cell_state: GridCellState, parent=None):
        super().__init__(parent)

        self._cell_state = cell_state
        self._x = x
        self._y = y
        self.init_layout()
        self.init_widgets()
        self.setObjectName("dummy")

    # paintEvent is overriden to make sure we can change background
    # color of custom widgets
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.update_style(self._cell_state)

    def update_style(self, cell_state: GridCellState):
        self._cell_state = cell_state
        if self._cell_state == GridCellState.SHIP:
            self.setStyleSheet("QWidget { background-color: red; }")
        elif self._cell_state == GridCellState.WATER:
            self.setStyleSheet("QWidget { background-color: blue; }")
        elif self._cell_state == GridCellState.HIT:
            self.setStyleSheet("QWidget { background-color: green; }")
        elif self._cell_state == GridCellState.MISS:
            self.setStyleSheet("QWidget { background-color: purple; }")
        elif self._cell_state == GridCellState.WAITING:
            self.setStyleSheet("QWidget { background-color: white; }")
