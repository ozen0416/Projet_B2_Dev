from typing import List

from src.Battleships.Game.ship import Ship
from src.Battleships.Tools import Vector2, Status, FromDictMixin


class Player(FromDictMixin):
    _ships: List[Ship]
    """
    Class for each player to keep track of the ships a player has

    - `ships`: List of all the ships of the player
    """
    def __init__(self, ships: List[Ship]) -> None:
        self._ships = ships

    def check_ship_hit(self, pos: Vector2) -> Status:
        status = Status.MISS
        for ship in self._ships:
            status = ship.check_for_hit(pos)
            if status != Status.MISS:
                break
        return status

    def __repr__(self):
        ships_str = [str(ship) for ship in self._ships]
        return f"Player({', '.join(ships_str)})"
