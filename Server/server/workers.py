import json
from typing import Any, Optional

from .abc import AbstractWorker

from .network import Server, Client, Pair


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

        mm_list = Server.get_instance().mm_list

        mm_list.append(client)

        print(mm_list)

        if len(mm_list) == 2:
            pair = Pair(mm_list[0], mm_list[1])
            Server.get_instance()._pairs.append(pair)

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
        pass
