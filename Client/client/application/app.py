import uuid

from PySide6.QtWidgets import QApplication, QWidget
from .windows import GameWindow, HomeWindow
from ..network import Client


class App(QApplication):
    _window: QWidget
    _socket_client: Client
    _client_id: str

    def __init__(self, arg__1: list):
        super().__init__(arg__1)
        self._window = GameWindow()
        with open("./styles/style.qss", 'r', encoding="utf-8") as theme:
            self.setStyleSheet(theme.read())
        # self._window = HomeWindow()
        self._window.show()

        self._client_id = str(uuid.uuid4())
        self.late_init()

    def late_init(self):
        self._socket_client = Client()

    @property
    def socket_client(self):
        return self._socket_client

    @property
    def user(self):
        return "ozen"

    @property
    def client_id(self):
        return self._client_id
