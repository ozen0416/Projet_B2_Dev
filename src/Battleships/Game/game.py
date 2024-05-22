"""Game manager for our battleships game"""
from src.Battleships.Tools import FromDictMixin, Vector2


class Game(FromDictMixin):
    """
    Game Manager, stores all required data for the
    game to be functional. Also contains methods to
    instantiate and make the game progress

    `first_player`: Player 1 of the game
    `second_player`: Player 2 of the game
    `turn`: Current turn of the game
    """

    first_player: str
    second_player: str
    turn: int

    def __init__(self, *args, **kwargs):
        pass

    def init_ships(self, player, size, cells_pos):
        pass

    def process_attack(self):
        pass

    def process_turn(self, target_cell: Vector2):
        attacked_player = self.turn % 2

    def __repr__(self):
        return f"Game(first_player: {self.first_player}, second_player: {self.second_player}, turn: {self.turn})"
