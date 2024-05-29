import threading
import json
import time
import uuid
import socket
from PySide6.QtCore import QObject, Slot, Signal


HOST = '2.9.106.99'
PORT = 4704

client_id = str(uuid.uuid4())

data = {
    "request": ["MATCHMAKING", "IN"],
    "client_id": client_id
}

ship_cells = [{"_pos": {"_x": 0, "_y": 1}}, {"_pos": {"_x": 0, "_y": 2}}, {"_pos": {"_x": 0, "_y": 3}}]

data_placement = {
    "request": ["GAME", "PLACEMENT"],
    "client_id": client_id,
    "data": {"_ships": [{"_size": 3, "_pos": {"_x": 0, "_y": 1}, "_ship_cells": ship_cells}]}
}


data_message = {
    "request": ["GAME", "MESSAGE"],
    "client_id": client_id,
    "data": {"content": "test message"}
}


def dict_to_encoded_utf_8(_dict: dict):
    json_dict = json.dumps(_dict)
    return json_dict.encode('utf-8')


class Client(QObject):
    """
    Client application side that will communicate and listen
    for the server requests.
    """
    _socket: socket.socket
    data_received = Signal(dict)

    def __init__(self):
        super().__init__()
        # self.__SERVER_IP = '2.9.106.99'
        # self.__SERVER_PORT = 4704
        self.__SERVER_IP = 'localhost'
        self.__SERVER_PORT = 39688

        self.start()
        self.running = True

    def start(self):
        """
        start the client socket communication with the server
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._socket.connect((self.__SERVER_IP, self.__SERVER_PORT))

    def send_request(self, request: dict):
        formatted_request = dict_to_encoded_utf_8(request)
        self._socket.send(formatted_request)

    @Slot()
    def listen(self):
        """
        listen for server requests
        """
        while self.running:
            response = self._socket.recv(1024).decode('utf-8')
            json_response = json.loads(response)
            print(json_response)
            if "request" in json_response:
                self.data_received.emit(json_response)

    @Slot()
    def stop(self):
        """
        Try to ensure closing connection when client object is deleted.
        Actually not really safe as we do not practically know where or if this will be called
        """
        self.running = False
        if self._socket:
            self._socket.close()
