import uuid

from .client import Client
from ..game import Game
from ..tools import Vector2


class Pair:
    """
    A `Pair` is a set of few things:
        - The current `Game` instance to process the game and keep a track of its different states.
        - An `ID` that will link our client requests to the game also serving as a game ID
        - A `FirstClient`
        - A `SecondClient`
    """
    game: Game
    game_id: str
    first_client: Client
    second_client: Client

    def __init__(self, first_client: Client, second_client: Client):
        self.id = str(uuid.uuid4())
        self.first_client = first_client
        self.second_client = second_client

    async def client_placement(self, request: dict):
        """
        Called by `PlacementWorker` when a client requests for his placement
        """
        client_id = request["client_id"]
        client = await self.get_client_by_id(client_id)
        if client is None:
            raise Exception("client not in pair")
        client.ships_data = request["data"]
        if self.first_client.ships_data is not None and self.second_client.ships_data is not None:
            await self.start_game()
            return "GAME START"
        return "WAIT FOR OTHER CLIENT"

    async def client_hit(self, request: dict):
        """
        Called by `HitWorker` when a client requests to hit a target cell
        on the enemy side.
        """
        client_id = request["client_id"]
        client = await self.get_client_by_id(client_id)
        if client is None:
            raise Exception("client not in pair")

        target_cell = Vector2.from_dict(request["data"])
        return self.game.process_turn(target_cell)

    async def start_game(self):
        """
        Only called when both clients have set up their ships and
        told the server.
        """
        print("START GAME CALLED")
        data = {
            "first_player": self.first_client.ships_data,
            "second_player": self.second_client.ships_data
        }

        self.game = Game.from_dict(data)

    async def get_client_by_id(self, _id: str):
        if not self.is_id_in_pair(_id):
            return None
        if id == self.first_client.id:
            return self.first_client
        return self.second_client

    async def is_id_in_pair(self, _id: str):
        return self.first_client.id == _id or self.second_client.id == _id
