import json
from typing import Any, Optional

from PySide6.QtWidgets import QApplication

from .abc import AbstractWorker
from .tools import GameState


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


class GameStartWorker(AbstractWorker):
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        QApplication.instance().current_window.start_game(request)

        response = {"status": "OK", "response": "GAME START RECEIVED OK"}

        return response


class GameFinishedWorker(AbstractWorker):
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        QApplication.instance().current_window.update_state(GameState.FINISHED)

        response = {"status": "OK", "response": "GAME FINISHED RECEIVED OK"}

        return response


class HitResponseWorker(AbstractWorker):
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        QApplication.instance().current_window.update_enemy_grid(request["data"])

        QApplication.instance().current_window.update_state(GameState.WAITING)

        response = {"status": "OK", "response": "HIT RESPONSE RECEIVED OK"}

        return response


class HitRequestWorker(AbstractWorker):
    def handle(self, request_type: Any, request: Any) -> Optional[dict]:
        QApplication.instance().current_window.update_ally_grid(request["data"])

        QApplication.instance().current_window.update_state(GameState.PROGRESS)
        response = {"status": "OK", "response": "HIT REQUEST RECEIVED OK"}

        return response
