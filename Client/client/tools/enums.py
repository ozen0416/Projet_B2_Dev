from enum import Enum


class ButtonState(Enum):
    PLAY = 1
    CANCEL = 2


class GridCellState(Enum):
    WATER = 0
    SHIP = 1
