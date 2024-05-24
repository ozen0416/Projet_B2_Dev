"""File containing every handler we will use in our chain of responsibility."""
from typing import Any, Optional

from .abc import AbstractHandler, AbstractWorker
from .workers import HitWorker


class RootHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("GAME", GameHandler())


class GameHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("HIT", HitWorker())

