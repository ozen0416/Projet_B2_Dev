from typing import List


class Queue:
    """
    Queue class is intended to work as a matchmaking system handler
    """
    def __init__(self):
        self.waiting_clients: List = []

    async def add_client(self, client):
        """
        Add a client to the current waiting clients list
        """
        self.waiting_clients.append(client)

    async def remove_client(self, client):
        """
        Remove a specific client from the clients list
        """
        if client in self.waiting_clients:  # To avoid value error even if requests goes through
            self.waiting_clients.remove(client)

    async def match_players(self):
        """
        Returns a tuple of clients if there is a match
        otherwise returns None
        """
        if len(self.waiting_clients) >= 2:
            client0 = self.waiting_clients.pop(0)
            client1 = self.waiting_clients.pop(0)
            return client0, client1
        return None
