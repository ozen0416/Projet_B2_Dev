import asyncio

from Network import Client

if __name__ == "__main__":
    client = Client()
    asyncio.run(client.start())
