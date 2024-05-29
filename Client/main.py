import sys

from client import App

if __name__ == "__main__":
    #client = HTTPClient()
    #asyncio.run(client.start())

    app = App([])
    sys.exit(app.exec())
