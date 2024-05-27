"""File containing every handler we will use in our chain of responsibility."""
from typing import Any, Optional

from .abc import AbstractHandler
from .workers import HitWorker, MatchmakingInWorker, MatchmakingOutWorker


class RootHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("GAME", GameHandler())


class GameHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("HIT", HitWorker())


class MatchmakingHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("IN", MatchmakingInWorker())
        self.add_tree_object("OUT", MatchmakingOutWorker())
