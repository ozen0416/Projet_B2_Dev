from src.Battleships.Game import Game
from src.Battleships.Tools import Vector2

ship_cells = [{"_pos": Vector2(0, 1), "_is_hit": False}, {"_pos": Vector2(0, 2), "_is_hit": False}, {"_pos": Vector2(0, 3), "_is_hit": False}]
ship1_cells = [{"_pos": Vector2.one(), "_is_hit": False}]


data = {
    "first_player": {"_ships": [{"_size": 3, "_pos": Vector2(0, 1), "_ship_cells": ship_cells, "_is_sunk": False}]},

    "second_player": {"_ships": [{"_size": 3, "_pos": Vector2(0, 1), "_ship_cells": ship_cells, "_is_sunk": False},
                                 {"_size": 1, "_pos": Vector2(1, 1), "_ship_cells": ship1_cells, "_is_sunk": False}]},

    "turn": 0
}

game = Game.from_dict(data)

print(game.process_turn(Vector2.up())) # 1

print(game)

print(game.process_turn(Vector2.down())) # 2

print(game)

print(game.process_turn(Vector2(0, 2))) # 1

print(game)

print(game.process_turn(Vector2(0, 2))) # 2

print(game)

print(game.process_turn(Vector2(0, 3))) # 1

print(game)

print(game.process_turn(Vector2(0, 3))) # 2

print(game)

print(game.process_turn(Vector2.one())) # 1

print(game)
