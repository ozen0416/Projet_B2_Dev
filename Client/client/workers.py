import json
from typing import Any, Optional

from PySide6.QtWidgets import QApplication

from .abc import AbstractWorker


class GameFoundWorker(AbstractWorker):
    """
    HitWorker will give to the proper game instance of a pair
    the current turn processed by a player.
    """
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        print(f"REQUEST GAME FOUND HANDLER{request}")
        QApplication.instance().current_window.switch_window.emit("game", request["data"]["nickname"])
        response = {"status": "OK", "response": "GAME FOUND OK"}
        return response


class GameMessageWorker(AbstractWorker):
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        """
        Handle game message request and send it to other client
        """
        QApplication.instance().receive_message(request)

        response = {"status": "OK", "response": "MESSAGE RECEIVED OK"}
        return response
