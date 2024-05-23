import asyncio
import sys

from application.app import App
from Network import HTTPClient

if __name__ == "__main__":
    #client = HTTPClient()
    #asyncio.run(client.start())

    app = App([])
    sys.exit(app.exec())
