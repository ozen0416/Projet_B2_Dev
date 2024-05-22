"""Vector2 class for easier manipulation inside of game code of 2D coordinates"""
from __future__ import annotations


class Vector2:
    """
    Vector2 class for easier coordinates manipulation

    - `pos_x`: x position of the vector
    - `pos_y`: y position
    """
    def __init__(self, pos_x: int, pos_y: int):
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y

    @property
    def pos_x(self):
        """x position on the map"""
        return self._pos_x

    @property
    def pos_y(self):
        """y position on the map"""
        return self._pos_y

    @pos_x.setter
    def pos_x(self, value: int):
        self._pos_x = value

    @pos_y.setter
    def pos_y(self, value: int):
        self._pos_y = value

    def __eq__(self, other: Vector2):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y
