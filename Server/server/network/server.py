import asyncio
from asyncio import StreamWriter, StreamReader
from typing import Coroutine, Any

from ..handlers import RootHandler



class Server:
    def __init__(self) -> None:
        self._root_handler = RootHandler()

        self.__HOST = 'localhost'
        self.__PORT = 39688

    async def handle_client(self, reader: StreamReader, writer: StreamWriter) -> None:
        addr = writer.get_extra_info("peername")
        print(f"Connected with: {addr}")

        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                response = data.decode('utf-8')
                print(f"Data received {response}")

                writer.write(data)
                await writer.drain()
        except ConnectionResetError as cre:
            print(f"Error occured with client {addr}: {cre}")
        finally:
            writer.close()
            print(f"Closed connection with: {addr}")

    async def start(self):
        server = await asyncio.start_server(self.handle_client, self.__HOST, self.__PORT)
        print(f"Server listening on {self.__HOST}:{self.__PORT}")

        async with server:
            await server.serve_forever()
