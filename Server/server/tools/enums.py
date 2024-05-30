from enum import Enum


class Status(Enum):
    MISS = 0
    HIT = 1
    SUNK = 2
    ALL_SUNK = 3
