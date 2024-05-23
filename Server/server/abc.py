"""ABC file containing every abstract class of the server-side"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Handler interface for our chain of responsibility.
    """

    @abstractmethod
    def set_next(self, handler: Handler) ->  Handler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        """Returns a handler object so we can chain link handlers"""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
