import asyncio

from server import Server

if __name__ == "__main__":
    server = Server.get_instance()
    asyncio.run(server.start())
