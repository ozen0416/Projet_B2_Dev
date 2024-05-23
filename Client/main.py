import sys

from Client.client.application.app import App

if __name__ == "__main__":
    #client = HTTPClient()
    #asyncio.run(client.start())

    app = App([])
    sys.exit(app.exec())
