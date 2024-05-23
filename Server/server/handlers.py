"""File containing every handler we will use in our chain of responsibility."""
from typing import Any, Optional

from .abc import AbstractHandler, Handler


class RootHandler(AbstractHandler):
    def __init__(self):
        self.add_tree_object("GAME", GameHandler())

root_handler = RootHandler()

root_handler.handle("GAME", {})


class GameHandler(AbstractHandler):
    def __init__(self):
        pass
