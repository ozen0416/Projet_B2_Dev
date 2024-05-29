import json
from typing import Any, Optional

from .abc import AbstractWorker

from .network import Server, Pair


class HitWorker(AbstractWorker):
    """
    HitWorker will give to the proper game instance of a pair
    the current turn processed by a player.
    """
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pair = await Server.get_instance().get_pair_from_client_id(request["client_id"])
        return await pair.client_hit(request)


class PlacementWorker(AbstractWorker):
    """
    Gets the placement request of a client and add it to its pair data
    """
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pair = await Server.get_instance().get_pair_from_client_id(request["client_id"])
        return await pair.client_placement(request)


class MatchmakingInWorker(AbstractWorker):
    """
    This worker is intended to add the players to the matchmaking queue.
    """
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        client = await Server.get_instance().get_client_from_id(request["client_id"])

        queue = Server.get_instance().mm_queue
        await queue.add_client(client)

        pair = await queue.match_players()
        if pair is not None:
            Server.get_instance().create_pair(*pair)

        data = {
            "status": "OK",
            "response": "MATCHMAKING IN"
        }

        return json.dumps(data)


class MatchmakingOutWorker(AbstractWorker):
    """
    This worker is intended to remove the players to the matchmaking queue.
    """
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        client = await Server.get_instance().get_client_from_id(request["client_id"])

        queue = Server.get_instance().mm_queue
        await queue.remove_client(client)

        data = {
            "status": "OK",
            "response": "MATCHMAKING OUT"
        }

        return json.dumps(data)


class GameMessageWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        """
        Handle game message request and send it to other client
        """
        pair = await Server.get_instance().get_pair_from_client_id(request["client_id"])

        await pair.send_message(request)

        data = {
            "status": "OK",
            "response": "MESSAGE SENT"
        }

        return json.dumps(data)
