from enum import Enum


class ButtonState(Enum):
    PLAY = 0
    CANCEL = 1


class GridCellState(Enum):
    MISS = 0
    HIT = 1
    WATER = 2
    SHIP = 3
    WAITING = 4


class GameState(Enum):
    PLACEMENT = 0
    PROGRESS = 1
    FINISHED = 2
    WAITING = 3
