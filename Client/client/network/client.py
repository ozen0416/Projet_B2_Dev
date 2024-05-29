import threading
import json
import time
import uuid
import socket

HOST = 'localhost'
PORT = 39688

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


class Client:
    """
    Client application side that will communicate and listen
    for the server requests.
    """
    _socket: socket.socket

    def start(self):
        """
        start the client socket communication with the server
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._socket.connect((HOST, PORT))

        json_data = json.dumps(data)

        self._socket.send(json_data.encode('utf-8'))

        print(f"CLIENT DATA SENT: {data}")
        while True:
            self.listen()

    def listen(self):
        """
        listen for server requests
        """
        while True:
            response = self._socket.recv(1024).decode('utf-8')
            json_response = json.loads(response)
            print(json_response)

            if json_response["response"] == "GAME FOUND":
                encoded_data = dict_to_encoded_utf_8(data_placement)

                self._socket.send(encoded_data)
                print(f"CLIENT DATA SENT: {data_placement}")

                response = self._socket.recv(1024).decode('utf-8')
                json_response = json.loads(response)
                print(f"CLIENT RESPONSE RECEIVED: {json_response}")

                encoded_data = dict_to_encoded_utf_8(data_message)
                self._socket.send(encoded_data)
                print(f"CLIENT DATA SENT: {data_message}")

                response = self._socket.recv(1024).decode('utf-8')
                json_response = json.loads(response)
                print(f"CLIENT RESPONSE RECEIVED: {json_response}")

    def __del__(self):
        """
        Try to ensure closing connection when client object is deleted.
        Actually not really safe as we do not practically know where or if this will be called
        """
        self._socket.close()
