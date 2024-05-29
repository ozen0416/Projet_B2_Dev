import json
import asyncio
from asyncio import StreamWriter, StreamReader
from typing import List, Optional

from .pair import Pair
from .client import Client
from ..matchmaking import Queue


class Server:
    """
    Server class, handling clients sockets and requests.
    """

    _instance = None

    def __init__(self) -> None:
        from ..handlers import RootHandler
        self._root_handler: RootHandler = RootHandler()

        self.__HOST: str = 'localhost'
        self.__PORT: int = 39688

        self._pairs: List[Pair] = []
        self._clients: List[Client] = []
        self.mm_queue = Queue()

    @staticmethod
    def get_instance():
        """
        As server is meant to be a Singleton, for easier access through the
        architecture and object instances.
        """
        if Server._instance is None:
            Server._instance = Server()
        return Server._instance

    async def create_pair(self, client_0, client_1):
        pair = Pair(client_0, client_1)
        await pair.init_pair()
        self.add_pair(pair)

    async def handle_client(self, reader: StreamReader, writer: StreamWriter) -> None:
        """
        Called each time a new socket is initialized with a client
        It will create the client object properly by using connection and socket received
        data.

        Each request will be sent to the `RootHandler` that will then properly handle what to respond.
        """
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
                client.id = json_response["client_id"]
                print(f"Data received {json_response}")
                if "request" in json_response:
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
        """
        start the asyncio server
        """
        server = await asyncio.start_server(self.handle_client, self.__HOST, self.__PORT)
        print(f"Server listening on {self.__HOST}:{self.__PORT}")

        async with server:
            await server.serve_forever()

    async def get_pair_from_client_id(self, _id: str) -> Optional[Pair]:
        for pair in self._pairs:
            if await pair.is_id_in_pair(_id):
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

    def add_pair(self, pair: Pair):
        self._pairs.append(pair)
