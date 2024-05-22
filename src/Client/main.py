import asyncio

from Network import HTTPClient

if __name__ == "__main__":
    client = HTTPClient()
    asyncio.run(client.start())
