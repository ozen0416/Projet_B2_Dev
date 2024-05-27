from typing import Any, Optional

from .abc import AbstractWorker

from .network import Server, Client, Pair


class HitWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pair = Server.get_instance().get_pair_from_client_id(request["client_id"])
        return await pair.client_hit(request)


class PlacementWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pair = Server.get_instance().get_pair_from_client_id(request["client_id"])
        return await pair.client_placement(request)


class MatchmakingInWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:

        client = Server.get_instance().get_client_from_id(request["client_id"])

        mm_list = Server.get_instance().mm_list

        mm_list.append(client)

        if len(mm_list) == 2:
            pair = Pair(mm_list[0], mm_list[1])
            Server.get_instance()._pairs.append(pair)

        return "OK"


class MatchmakingOutWorker(AbstractWorker):
    async def handle(self, request_type: Any, request: Any) -> Optional[str]:
        pass
