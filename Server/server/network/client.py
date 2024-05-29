from dataclasses import dataclass
from asyncio import StreamWriter, StreamReader


@dataclass
class Client:
    """
    A Client server-side is a connected socket
    We represent it as a dataclass here as it will just
    be kept alive by the server for correct request handling.

    It has more data than just IP and PORT, it also
    stores the ID of the client, so we can be sure
    about if the request by that ID is legit.
    """
    ip: str
    port: int
    id: str
    reader: StreamReader
    writer: StreamWriter
    ships_data: dict

    def __init__(self, ip="", port=0, _id="", reader=None, writer=None, ships_data=None):
        self.ip = ip
        self.port = port
        self.id = _id
        self.reader = reader
        self.writer = writer
        self.ships_data = ships_data
