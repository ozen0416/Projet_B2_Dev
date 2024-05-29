from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout, QPushButton, QFrame, QStyleOption, QStyle
from PySide6.QtCore import Qt
from typing import Optional

from ....tools import GridCellState


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


class GridCell(QWidget):
    """
    Single Cell meant to be part of a Grid

    The Cell can have the state WATER or the state SHIP
    """

    def __init__(self, x: int, y: int, cell_state: GridCellState, parent=None):
        super().__init__(parent)

        self.label = QLabel(str(x) + str(y), self)
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

    """
    Event that shows coordinates of where the mouse presses
    """

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("je clique sur", self._x, self._y)
        return super().mousePressEvent(event)

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.layout().addWidget(self.label, Qt.AlignCenter)
        if self._cell_state == GridCellState.SHIP:
            self.setStyleSheet("QWidget { background-color: red; }")
        else:
            self.setStyleSheet("QWidget { background-color: blue; }")


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
