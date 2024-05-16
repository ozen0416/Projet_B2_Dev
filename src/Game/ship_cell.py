"""ShipCell python file"""

class ShipCell:
    """
    ShipCell class, intended to store
    informations about a cell of a ship

    - `pos_x`: x position on the map
    - `pos_y`: y position on the map
    - `is_hit`: whether or not the cell has been hit
    """
    def __init__(self, pos_x: int, pos_y: int, is_hit: bool=False):
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y
        self._is_hit: bool = is_hit

    @property
    def pos_x(self):
        """x position on the map"""
        return self._pos_x

    @property
    def pos_y(self):
        """y position on the map"""
        return self._pos_y

    @property
    def is_hit(self):
        """whether or not the cell has been hit"""
        return self._is_hit

    @is_hit.setter
    def is_hit(self, value: bool):
        self._is_hit = value
