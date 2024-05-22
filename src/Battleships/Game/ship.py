from typing import List

from ship_cell import ShipCell
from src.Battleships.Tools.enums import Status
from ..Tools import Vector2


class Ship:
    """
    Ship class, intended to keep track of individual ShipCell.

    - `size`: the number of cells in the ship 
    - `pos`: Vector2 of the position of the first cell of the ship on the map
    - `vertical`: *optional* is the ship placed vertically or not on the map
    - `ship_cells`: A list of ShipCell objects
    - `is_sunk`: whether the ship is sunk or not 

    """
    def __init__(self, size: int, pos: Vector2, vertical: bool = False) -> None:
        self._size:         int = size
        self._pos:          Vector2 = pos
        self._ship_cells:   List[ShipCell] = []
        self._is_sunk:      bool = False

        for i in range(self._size):
            if vertical:
                ship_cell = ShipCell(self._pos + Vector2(0, i))
            else:
                ship_cell = ShipCell(self._pos + Vector2(i, 0))

            self._ship_cells.append(ship_cell)

    @property
    def pos(self) -> Vector2:
        """x position on the map"""
        return self._pos

    @property
    def size(self) -> int:
        """size of the ship, wich is its number of cells"""
        return self._size

    @property
    def is_sunk(self) -> bool:
        """returns if the ship has been sunk"""
        return self._is_sunk

    def check_for_hit(self, pos: Vector2) -> Status:
        status = Status.MISS
        for cell in self._ship_cells:
            if cell.check_for_hit(pos):
                status = Status.HIT
                break
        if self.check_for_sunk(): status = Status.SUNK
        return status

    def check_for_sunk(self) -> bool:
        for cell in self._ship_cells:
            if not cell.is_hit:
                return False 
        self._is_sunk = True 
        return True
