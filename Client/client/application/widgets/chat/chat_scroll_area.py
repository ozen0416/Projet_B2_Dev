from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import Qt

from .chat_area import ChatArea


class ChatScrollArea(QScrollArea):
    def __init__(self, contact, parent=None):
        super().__init__(parent)
        self.setObjectName('ChatScrollArea')

        self._chat_area = ChatArea(contact, parent=self)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.init_widgets()

    def init_widgets(self):
        self.setWidget(self._chat_area)
        self.setWidgetResizable(True)

    def add_textbox_from_message(self, message):
        self._chat_area.add_textbox_from_message(message)
