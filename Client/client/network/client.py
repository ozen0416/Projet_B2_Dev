import json
import uuid
import socket

HOST = 'localhost'
PORT = 39688


class Client:
    _socket: socket.socket

    async def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._socket.connect((HOST, PORT))

        data = {
            "request": ["MATCHMAKING", "IN"],
            "client_id": uuid.uuid4(),
            "ip": "172.33.10.21",
            "port": 22
        }

        try:
            json_data = json.dumps(data)

            self._socket.send(json_data.encode('utf-8'))

            print(f"CLIENT DATA SENT: {data}")

            response = self._socket.recv(1024).decode('utf-8')
            print(f"CLIENT RESPONSE RECEIVED: {response}")

            if response == "OK":
                response = self._socket.recv(1024).decode('utf-8')
                data["request"] = ["GAME", "HIT"]
                data["game_id"] = ""
                data["data"] = {"_x": 0, "_y": 1}
        finally:
            self._socket.close()
            print("CLIENT CONNECTION CLOSED")

    def __del__(self):
        self._socket.close()
