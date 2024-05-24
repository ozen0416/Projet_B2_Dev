import asyncio

from client.network import Client

if __name__ == "__main__":
    client = Client()
    asyncio.run(client.start())

