from enum import IntEnum


class Status(IntEnum):
    MISS = 0
    HIT = 1
    SUNK = 2
    ALL_SUNK = 3
