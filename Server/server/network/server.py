import json
import asyncio
from asyncio import StreamWriter, StreamReader
from typing import List, Optional

from .pair import Pair
from .client import Client


class Server:
    _instance = None

    @staticmethod
    def get_instance():
        if Server._instance is None:
            Server._instance = Server()
        return Server._instance

    def __init__(self) -> None:
        from ..handlers import RootHandler
        self._root_handler: RootHandler = RootHandler()

        self.__HOST: str = 'localhost'
        self.__PORT: int = 39688

        self._pairs: List[Pair] = []
        self._clients: List[Client] = []
        self.mm_list = []

    async def handle_client(self, reader: StreamReader, writer: StreamWriter) -> None:
        addr = writer.get_extra_info("peername")
        print(f"Connected with: {addr}")
        print(type(addr))

        client = Client(ip=addr[0], port=addr[1],reader=reader, writer=writer)
        self._clients.append(client)

        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                response = data.decode('utf-8')
                json_response = json.loads(response)
                print(f"Data received {json_response}")
                request_base = json_response["request"][0]
                print("Sending to RootHandler...")
                res = await self._root_handler.handle(request_base, json_response)
                print(f"Worker response: {res}")

                writer.write(res.encode('utf-8'))
                await writer.drain()
        except ConnectionResetError as cre:
            print(f"Error occurred with client {addr}: {cre}")
        finally:
            writer.close()
            print(f"Closed connection with: {addr}")

    async def start(self):
        server = await asyncio.start_server(self.handle_client, self.__HOST, self.__PORT)
        print(f"Server listening on {self.__HOST}:{self.__PORT}")

        async with server:
            await server.serve_forever()

    async def get_pair_from_client_id(self, _id: str) -> Optional[Pair]:
        for pair in self._pairs:
            if pair.is_id_in_pair(_id):
                return pair
        return None

    async def get_pair_from_game_id(self, _id: str) -> Optional[Pair]:
        for pair in self._pairs:
            if pair.game_id == _id:
                return pair
        return None

    async def get_client_from_id(self, _id: str) -> Optional[Client]:
        for client in self._clients:
            if client.id == _id:
                return client
        return None

    async def add_pair(self, pair: Pair):
        self._pairs.append(pair)
