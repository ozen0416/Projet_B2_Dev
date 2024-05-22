import asyncio

from Network import HTTPServer

if __name__ == "__main__":
    server = HTTPServer()
    asyncio.run(server.start())
