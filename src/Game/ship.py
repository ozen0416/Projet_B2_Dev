from ship_cell import ShipCell

class Ship:
    """
    Ship class, intended to keep track of individual ShipCell.

    - `size`: the number of cells in the ship 
    - `pos_x`: x position of the first cell of the ship on the map
    - `pos_y`: y position of the first cell of the ship on the map
    - `vertical`: *optional* is the ship placed vertically or not on the map

    """
    def __init__(self, size:int, pos_x:int, pos_y:int, vertical:bool=False) -> None:
        self._size = size
        self._pos_x = pos_x
        self._pos_y = pos_y

        self._ship_cells = []

        for i in range(self._size):
            if vertical:
                ship_cell = ShipCell(self._pos_x, self._pos_y + i)
            else:
                ship_cell = ShipCell(self._pos_x + i, self._pos_y)
            
            self._ship_cells.append(ship_cell)

    @property
    def pos_x(self):
        """x position on the map"""
        return self._pos_x

    @property
    def pos_y(self):
        """y position on the map"""
        return self._pos_y

    @property
    def size(self):
        """size of the ship, wich is its number of cells"""
        return self._size

    @property
    def is_sunk(self) -> bool:
        for cell in self._ship_cells:
            if not cell.is_hit():
                return False
        return True
