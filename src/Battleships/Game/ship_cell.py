"""ShipCell python file"""
from ..Tools import Vector2


class ShipCell:
    """
    ShipCell class, intended to store
    information about a cell of a ship

    - `pos`: x, y position on the map
    - `is_hit`: whether the cell has been hit
    """
    def __init__(self, pos: Vector2, is_hit: bool=False):
        self._pos: Vector2 = pos
        self._is_hit: bool = is_hit

    @property
    def pos(self):
        """x position on the map"""
        return self._pos

    @property
    def is_hit(self):
        """whether or not the cell has been hit"""
        return self._is_hit

    @is_hit.setter
    def is_hit(self, value: bool):
        self._is_hit = value

    def check_for_hit(self, pos: Vector2) -> bool:
        """check if cell is hit. if so change `is_hit` and return True"""
        if pos == self.pos:
            self.is_hit = True
            return True
        return False
