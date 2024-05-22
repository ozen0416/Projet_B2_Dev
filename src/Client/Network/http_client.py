import socket

HOST = 'localhost'
PORT = 39688


class HTTPClient:
    async def start(self):
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        _socket.connect((HOST, PORT))

        try:
            while True:
                data = '{"HIT": (0, 1)}'

                _socket.send(data.encode('utf-8'))

                print(f"CLIENT DATA SENT: {data}")

                response = _socket.recv(1024).decode('utf-8')
                print(f"CLIENT RESPONSE RECEIVED: {response}")
        finally:
            _socket.close()
            print("CLIENT CONNECTION CLOSED")

