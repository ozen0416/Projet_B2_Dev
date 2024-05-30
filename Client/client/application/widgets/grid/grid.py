import sys

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import Signal
from typing import Optional

from ....dataclasses import Ship, Cell
from ....tools import GridCellState
from .grid_cell import GridCell


class Grid(QWidget):
    """
    A grid of multiple GridCell
    Instantiate all GridCell as WATER

    Once there are 5 placed ships, the data of the ships is sent to the server

    Whenever a ship is place emit a Signal that will be catched by every Ship
    """

    ship_dropped = Signal(int)

    def __init__(self, size: int, parent: Optional[QWidget] = None, ally_grid: bool = False) -> None:
        super().__init__(parent)
        self.buttons = []
        self._size = size
        self.ally_grid = ally_grid

        self.placed_ships = []

        self.init_layout()
        self.init_grid_button()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if not self.ally_grid:
            return
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if not event.mimeData().hasText():
            return
        if not self.ally_grid:
            return

        ship_size = int(event.mimeData().text())
        print("DROPEVENT", ship_size)
        position = self.childAt(event.pos())
        if isinstance(position, GridCell):
            start_row, start_col = position._x, position._y
            self.place_ship(ship_size, start_row, start_col)
        event.acceptProposedAction()

    def place_ship(self, size, start_row, start_col):
        # Check if ship goes out of bounds
        if start_row + size > self._size:
            return

        # Check for overlapping ship
        for i in range(size):
            cell = self.layout().itemAtPosition(start_row + i, start_col).widget()
            if cell._cell_state == GridCellState.SHIP:
                return

        # Set cells as ships and emit signal that ship is dropped
        start_cell = Cell(start_row, start_col)
        cells = []
        for i in range(size):
            cur_row = start_row + i
            cells.append(Cell(cur_row, start_col))
            cell = self.layout().itemAtPosition(cur_row, start_col).widget()
            cell.update_style(GridCellState.SHIP)
        self.ship_dropped.emit(size)

        ship = Ship(size, start_cell, cells)
        self.placed_ships.append(ship)

    def update_grid_state(self, x: int, y: int, state: GridCellState):
        cell = self.layout().itemAtPosition(x, y)
        cell.update_styles(state)

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

    def __init__(self, title: str, parent=None, ally_grid: bool = False):
        super().__init__(parent)

        self.label = QLabel(title, self)
        self.grid = Grid(10, self, ally_grid)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def init_widgets(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.grid)


    """
    ship_cells = [{"_pos": {"_x": 0, "_y": 1}}, {"_pos": {"_x": 0, "_y": 2}}, {"_pos": {"_x": 0, "_y": 3}}]
    """
    def get_placement(self):
        placement = []
        for ship in self.grid.placed_ships:
            placement.append(ship.to_dict())
        return placement