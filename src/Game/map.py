class Map:
    """
    Class Map is intended to keep track of position of ships

    - `size`: is the size of the matrix
    - `map_matrix` is a 2D list used to have coordinates

    """
    def __init__(self, size) -> None:
        self._size = size
        self._map_matrix = [ [None] * self._size ] * self._size

    @property
    def map_matrix(self):
        return self._map_matrix
