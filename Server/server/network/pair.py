import asyncio
import json
import uuid

from .client import Client
from ..game import Game
from ..tools import Vector2, Status


class Pair:
    """
   A `Pair` is a set of few things:
        - The current `Game` instance to process the game and keep a track of its different states.
        - An `id` that will be the game id
        - A First `Client`
        - A Second `Client`
    """
    game: Game
    game_id: str
    first_client: Client
    second_client: Client

    def __init__(self, first_client: Client, second_client: Client):
        self.game_id = str(uuid.uuid4())
        self.first_client = first_client
        self.second_client = second_client

        print(f"PAIR INIT: {self.first_client.id}, {self.second_client.id}")

    async def init_pair(self):
        """
        Extension to `__init__` call
        will send to both clients that they
        were matched in a game
        """
        data = {
            "request": ["GAME", "FOUND"],
            "data": {"nickname": self.first_client.nickname, "game_id": self.game_id}
        }
        json_data = json.dumps(data)

        await self.second_client.send_data(json_data.encode('utf-8'))

        data["data"]["nickname"] = self.second_client.nickname
        json_data = json.dumps(data)

        await self.first_client.send_data(json_data.encode('utf-8'))

    async def client_placement(self, request: dict):
        """
        Called by `PlacementWorker` when a client requests for his placement
        """
        client_id = request["client_id"]
        client = await self.get_client_by_id(client_id)
        if client is None:
            raise Exception("client not in pair")
        client.ships_data = request["data"]

        print("CLIENTS SHIPS DATA:")
        print(self.first_client.ships_data)
        print(self.second_client.ships_data)
        if self.first_client.ships_data and self.second_client.ships_data:
            await self.start_game()

        data = {
            "status": "OK",
            "response": "PLACEMENT OK"
        }

        json_data = json.dumps(data)

        return json_data

    async def client_hit(self, request: dict):
        """
        Called by `HitWorker` when a client requests to hit a target cell
        on the enemy side.
        """
        client_id = request["client_id"]
        client = await self.get_client_by_id(client_id)
        if client is None:
            raise Exception("client not in pair")

        request_pos = request["data"]["_pos"]

        target_cell = Vector2(request_pos["_x"], request_pos["_y"])

        turn_result = self.game.process_turn(target_cell)
        turn_result = int(turn_result)

        data = {
            "status": "OK",
            "request": ["GAME", "HIT_RESPONSE"],
            "data": request["data"]
        }

        data["data"]["status"] = turn_result

        paired_data = {
            "request": ["GAME", "HIT_REQUEST"],
            "data": request["data"]
        }

        paired_data["data"]["status"] = turn_result

        json_data = json.dumps(data)
        paired_json_data = json.dumps(paired_data)

        paired_client = self._get_paired_client(client_id)
        await paired_client.send_data(paired_json_data.encode('utf-8'))

        if turn_result == Status.ALL_SUNK:
            await self.game_finish()

        return json_data

    async def game_finish(self):
        data = {
            "request": ["GAME", "FINISHED"]
        }

        json_data = json.dumps(data)
        encoded_data = json_data.encode('utf-8')

        await self.first_client.send_data(encoded_data)

        await self.second_client.send_data(encoded_data)

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

        data = {
            "request": ["GAME", "START"],
            "data": {"start": True}
        }

        json_data = json.dumps(data)
        encoded_data = json_data.encode('utf-8')

        await self.first_client.send_data(encoded_data)

        data["data"]["start"] = False
        json_data = json.dumps(data)
        encoded_data = json_data.encode('utf-8')

        await self.second_client.send_data(encoded_data)

    async def send_message(self, request: dict):
        client_id = request["client_id"]
        paired_client = self._get_paired_client(client_id)

        data = {
            "data": request["data"],
            "request": ["GAME", "MESSAGE"],
            "nickname": request["nickname"]
        }

        data["data"]["nickname"] = paired_client.nickname
        json_data = json.dumps(data)

        paired_client.writer.write(json_data.encode('utf-8'))
        await paired_client.writer.drain()

    def _get_paired_client(self, client_id: str):
        return self.first_client if client_id == self.second_client.id else self.second_client

    async def get_client_by_id(self, _id: str):
        if not await self.is_id_in_pair(_id):
            return None
        if _id == self.first_client.id:
            return self.first_client
        return self.second_client

    async def is_id_in_pair(self, _id: str):
        return self.first_client.id == _id or self.second_client.id == _id
