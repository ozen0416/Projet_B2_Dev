"""File containing every handler we will use in our chain of responsibility."""
from typing import Any, Optional

from .abc import AbstractHandler
from .workers import (
    GameFoundWorker,
    GameMessageWorker,
    GameStartWorker,
    GameFinishedWorker,
    HitRequestWorker,
    HitResponseWorker
)


class RootHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("GAME", GameHandler())


class GameHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("FOUND", GameFoundWorker())
        self.add_tree_object("MESSAGE", GameMessageWorker())
        self.add_tree_object("START", GameStartWorker())
        self.add_tree_object("HIT_RESPONSE", HitResponseWorker())
        self.add_tree_object("HIT_REQUEST", HitRequestWorker())
        self.add_tree_object("FINISHED", GameFinishedWorker())
