import json
import socket

HOST = 'localhost'
PORT = 39688


class Client:
    _socket: socket.socket

    async def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._socket.connect((HOST, PORT))

        try:
            while True:
                data = {
                    "request": ["GAME", "HIT"],
                    "data": {"_x": 0, "_y": 1}
                }

                json_data = json.dumps(data)

                self._socket.send(json_data.encode('utf-8'))

                print(f"CLIENT DATA SENT: {data}")

                response = self._socket.recv(1024).decode('utf-8')
                print(f"CLIENT RESPONSE RECEIVED: {response}")
        finally:
            self._socket.close()
            print("CLIENT CONNECTION CLOSED")

    def __del__(self):
        self._socket.close()
