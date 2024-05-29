"""ABC file containing every abstract class of the server-side"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional, Callable, List


class TreeObject(ABC):
    """Tree Object, being either a Handler or a Worker later"""
    @abstractmethod
    def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pass


class Handler(TreeObject, ABC):
    """
    Handler interface for our Tree request handling behavior.
    """
    _tree_objects: dict = {}
    _checks: List[Callable] = []

    @abstractmethod
    def add_tree_object(self, request_type: str, tree_object: TreeObject) -> None:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    def add_tree_object(self, request_type: str, tree_object: TreeObject) -> None:
        self._tree_objects[request_type] = tree_object

    def add_check(self, check: Callable):
        self._checks.append(check)

    def check(self, data):
        for check in self._checks:
            check(data)

    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        """
        The handle of the Handler is to pass through the tree the data.

        It also is intended to check

        this function is abstract, so you have to implement it to
        give it check decorators
        """
        self.check(request)

        if isinstance(request_type, str):
            request["request"].pop(0)

        request_type = request["request"][0]

        if request_type in self._tree_objects:
            res = self._tree_objects[request_type].handle(request_type, request)
            return res
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
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        return None
