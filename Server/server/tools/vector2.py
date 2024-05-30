"""Vector2 class for easier manipulation inside of game code of 2D coordinates"""
from __future__ import annotations

from .from_dict_mixin import FromDictMixin


class Vector2(FromDictMixin):
    """
    Vector2 class for easier coordinates manipulation

    - `x`: x position of the vector
    - `y`: y position
    """

    _x: int
    _y: int

    def __init__(self, x: int, y: int):
        self._x: int = x
        self._y: int = y

    @property
    def x(self):
        """x position on the map"""
        return self._x

    @property
    def y(self):
        """y position on the map"""
        return self._y

    @x.setter
    def x(self, value: int):
        self._x = value

    @y.setter
    def y(self, value: int):
        self._y = value

    @staticmethod
    def one():
        return Vector2(1,1)

    @staticmethod
    def zero():
        return Vector2(0,0)

    @staticmethod
    def up():
        return Vector2(0,1)

    @staticmethod
    def down():
        return Vector2(0,-1)

    @staticmethod
    def left():
        return Vector2(-1,0)

    @staticmethod
    def right():
        return Vector2(1,0)

    def equals(self, other):
        return self._x == other._x and self._y == other._y

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self._x * other.x, self._y * other.y)
        elif isinstance(other, int):
            return Vector2(self._x * other, self._y * other)
        else:
            raise TypeError("Multiplication is only supported between Vector2 instances or scalars.")

    def __eq__(self, other: Vector2):
        return self._x == other._x and self._y == other._y

    def __add__(self, other: Vector2):
        return Vector2(self._x + other._x, self._y + other._y)

    def __repr__(self):
        return f"Vector2(x: {self._x}, y: {self._y})"