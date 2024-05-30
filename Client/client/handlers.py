"""File containing every handler we will use in our chain of responsibility."""
from typing import Any, Optional

from .abc import AbstractHandler
from .workers import (
    GameFoundWorker,
    GameMessageWorker
)


class RootHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("GAME", GameHandler())


class GameHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("FOUND", GameFoundWorker())
        self.add_tree_object("MESSAGE", GameMessageWorker())
