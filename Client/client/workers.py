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
        QApplication.instance().current_window.switch_window.emit("game" )
        response = {"status": "OK", "response": "GAME FOUND OK"}
        return response


# class GameMessageWorker(AbstractWorker):
#     async def handle(self, request_type: Any, request: Any) -> Optional[str]:
#         """
#         Handle game message request and send it to other client
#         """
#         pair = await Server.get_instance().get_pair_from_client_id(request["client_id"])
#
#         await pair.send_message(request)
#
#         data = {
#             "status": "OK",
#             "response": "MESSAGE SENT"
#         }
#
#         return json.dumps(data)
