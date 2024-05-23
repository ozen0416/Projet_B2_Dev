"""ABC file containing every abstract class of the server-side"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, Callable, List


class TreeObject:
    """Tree Object, being either a Handler or a Worker later"""
    @abstractmethod
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pass


class Handler(TreeObject, ABC):
    """
    Handler interface for our Tree request handling behavior.
    """

    _tree_objects: dict = {}
    _checks: List[Callable] = []

    @abstractmethod
    async def add_tree_object(self, request_type: str, tree_object: TreeObject):
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    async def add_tree_object(self, request_type: str, handler: Handler) -> None:
        self._tree_objects[request_type] = handler

    async def add_check(self, check: Callable):
        self._checks.append(check)

    async def check(self, data):
        for check in self._checks:
            check(data)

    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        """
        The handle of the Handler is to pass through the tree the data.

        It also is intended to check

        this function is abstract, so you have to implement it to
        give it check decorators
        """

        await self.check(request)

        if request_type in self._tree_objects:
            return await self._tree_objects[request_type].handle(request_type, request)
        return None


class Worker(TreeObject, ABC):
    """Worker will process the data given to its handle method"""
    pass


class AbstractWorker(Worker):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    @abstractmethod
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        return None
