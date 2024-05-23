"""game manager for our battleships game"""
from Server.server.tools import FromDictMixin, Vector2, Status
from .player import Player


class Game(FromDictMixin):
    """
    game Manager, stores all required data for the
    game to be functional. Also contains methods to
    instantiate and make the game progress

    `first_player`: Player 1 of the game
    `second_player`: Player 2 of the game
    `turn`: Current turn of the game
    """

    first_player: Player
    second_player: Player
    turn: int
    finished: bool = False

    def process_turn(self, target_cell: Vector2):
        if self.finished:
            return

        self.turn += 1
        first_player_turn = self.turn % 2

        if first_player_turn:
            result = self.second_player.check_ship_hit(target_cell)
        else:
            result = self.first_player.check_ship_hit(target_cell)

        if result == Status.ALL_SUNK:
            self.finished = True

        return result

    def __repr__(self):
        return f"game(first_player: {self.first_player}, second_player: {self.second_player}, turn: {self.turn})"
