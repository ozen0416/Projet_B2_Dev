import asyncio
from typing import List

from ..network import Client


class Queue:
    def __init__(self):
        self.waiting_clients: List[Client] = []
        self.queue = asyncio.Queue()

    async def add_client(self, client: Client):
        self.waiting_clients.append(client)
        await self.match_players()

    async def remove_client(self, client: Client):
        if client in self.waiting_clients:
            self.waiting_clients.remove(client)

    async def match_players(self):
        if len(self.waiting_clients) >= 2:
            client1: Client = self.waiting_clients.pop(0)
            client2: Client = self.waiting_clients.pop(0)
            await self.queue.put()
