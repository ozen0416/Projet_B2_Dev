import json
import uuid

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QWidget

from ..network import Client
from .controller import Controller
from ..handlers import RootHandler


class App(QApplication):
    _window: QWidget
    _socket_client: Client
    _client_id: str
    _socket_thread: QThread

    def __init__(self, arg__1: list):
        super().__init__(arg__1)
        with open("./styles/style.qss", 'r', encoding="utf-8") as theme:
            self.setStyleSheet(theme.read())

        self._client_id = str(uuid.uuid4())
        self._controller = Controller()
        self._root_handler = RootHandler()
        self.late_init()

    @property
    def current_window(self):
        return self._controller.current_window

    def handle_request(self, request: dict):
        handler_response = self._root_handler.handle(request["request"], request)

        handler_response["client_id"] = self._client_id

        self._socket_client.send_request(handler_response)

    def late_init(self):
        self._socket_client = Client()
        self._socket_thread = QThread()
        self._socket_client.moveToThread(self._socket_thread)
        self._socket_thread.started.connect(self._socket_client.listen)
        self._socket_client.data_received.connect(self.handle_request)

        self.aboutToQuit.connect(self._socket_client.stop)
        self.aboutToQuit.connect(self._socket_thread.quit)
        self.aboutToQuit.connect(self._socket_thread.wait)
        self._socket_thread.start()

    @property
    def socket_client(self):
        return self._socket_client

    @property
    def user(self):
        return "ozen"

    @property
    def client_id(self):
        return self._client_id
