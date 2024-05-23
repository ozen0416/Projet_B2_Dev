import asyncio

from asyncio import StreamWriter, StreamReader


HOST = 'localhost'
PORT = 39688


class Server:

    async def handle_client(self, reader: StreamReader, writer: StreamWriter):
        addr = writer.get_extra_info("peername")
        print(f"Connected with: {addr}")

        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                response = data.decode('utf-8')
                print(f"Data received {response}")

                writer.write(data)
                await writer.drain()
        except ConnectionResetError as cre:
            print(f"Error occured with client {addr}: {cre}")
        finally:
            writer.close()
            print(f"Closed connection with: {addr}")

    async def start(self):
        server = await asyncio.start_server(self.handle_client, HOST, PORT)
        print(f"Server listening on {HOST}:{PORT}")

        async with server:
            await server.serve_forever()
