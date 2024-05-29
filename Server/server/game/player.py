from typing import List

from .ship import Ship
from ..tools import Vector2, Status, FromDictMixin


class Player(FromDictMixin):
    """
    Class for each player to keep track of the ships a player has

    - `ships`: List of all the ships of the player
    """

    _ships: List[Ship]

    def __init__(self, ships: List[Ship]) -> None:
        self._ships = ships

    def check_ship_hit(self, pos: Vector2) -> Status:
        status = Status.MISS
        for ship in self._ships:
            status = ship.check_for_hit(pos)
            if status != Status.MISS:
                print(f"\nPLAYER HIT 0: {str(self)}\n")
                break
        if status == Status.SUNK:
            status = self.check_all_sunk(status)

        return status

    def check_all_sunk(self, status) -> Status:
        for ship in self._ships:
            if not ship.is_sunk:
                return status
        print(f"ALL SUNK CHECK")
        return Status.ALL_SUNK


    def __repr__(self):
        ships_str = [str(ship) for ship in self._ships]
        return f"Player({', '.join(ships_str)})"
