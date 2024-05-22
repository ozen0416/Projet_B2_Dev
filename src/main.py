from src.Battleships.Game import Game

data = {
    "first_player": "a",
    "second_player": "b",
    "turn": 1
}

game = Game.from_dict(data)

print(game)
