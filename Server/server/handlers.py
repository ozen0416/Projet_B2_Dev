"""File containing every handler we will use in our chain of responsibility."""
from typing import Any, Optional

from .abc import AbstractHandler
from .workers import (
    HitWorker,
    MatchmakingInWorker,
    MatchmakingOutWorker,
    PlacementWorker,
    GameMessageWorker
)


class RootHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("GAME", GameHandler())
        self.add_tree_object("MATCHMAKING", MatchmakingHandler())


class GameHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("HIT", HitWorker())
        self.add_tree_object("PLACEMENT", PlacementWorker())
        self.add_tree_object("MESSAGE", GameMessageWorker())


class MatchmakingHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("IN", MatchmakingInWorker())
        self.add_tree_object("OUT", MatchmakingOutWorker())
