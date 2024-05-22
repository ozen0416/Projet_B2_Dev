"""Game manager for our battleships game"""
from src.Battleships.Tools import FromDictMixin


class Game(FromDictMixin):
    first_player: str
    second_player: str
    turn: int

    def __init__(self, *args, **kwargs):
        pass

    def init_ships(self, player, size, cells_pos):
        pass

    def process_attack(self):
        pass

    def process_turn(self, **kwargs):
        attacked_player = self.turn % 2

    def __repr__(self):
        return f"Game(first_player: {self.first_player}, second_player: {self.second_player}, turn: {self.turn})"
