import json
import uuid

from PySide6.QtCore import QThread, QSettings
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

        self._settings_file = QApplication.applicationDirPath() + "/settings.ini"


        self._user = ""
        self._client_id = ""  # str(uuid.uuid4())

        self.load_settings()
        self._controller = Controller()
        self._root_handler = RootHandler()

        self.late_init()

    def load_settings(self):
        settings = QSettings(self._settings_file, QSettings.IniFormat)
        nickname = settings.value("nickname", "")
        if nickname:
            self._user = nickname
        else:
            self._user = "DefaultNick"
        client_id = settings.value("client_id", "")
        if client_id:
            self._client_id = client_id
        else:
            self._client_id = str(uuid.uuid4())

    def save_settings(self):
        settings = QSettings(self._settings_file, QSettings.IniFormat)
        settings.setValue("nickname", self.user)
        settings.setValue("client_id", self._client_id)

    @property
    def current_window(self):
        return self._controller.current_window

    def send_request(self, request: dict):
        request["client_id"] = self._client_id
        request["nickname"] = self.user

        self._socket_client.send_request(request)

    def handle_request(self, request: dict):
        handler_response = self._root_handler.handle(request["request"], request)
        print(handler_response, type(handler_response))

        handler_response["client_id"] = self._client_id
        handler_response["nickname"] = self.user

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

    def receive_message(self, data: dict):
        self.current_window.receive_message(data)

    @property
    def socket_client(self):
        return self._socket_client

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
