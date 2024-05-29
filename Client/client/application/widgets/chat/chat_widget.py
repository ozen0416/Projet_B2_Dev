from PySide6.QtWidgets import QWidget, QGridLayout

from .chat_input_widget import ChatInputWidget
from .chat_scroll_area import ChatScrollArea


class ChatWidget(QWidget):
    def __init__(self, contact: str, parent=None):
        super().__init__(parent)

        self._contact = contact

        self._layout = QGridLayout(self)

        self._chat_scroll = ChatScrollArea(contact, self)
        self._chat_input = ChatInputWidget(contact, self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        self.setLayout(self._layout)

    def init_widgets(self):
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self._chat_scroll, 0, 0)
        self._layout.addWidget(self._chat_input, 1, 0)

    def showEvent(self, event):
        self._chat_input.setFocus()
        super().showEvent(event)

    def send_message(self):
        pass

    @property
    def chat_input(self):
        return self._chat_input

    @property
    def chat_scroll(self):
        return self._chat_scroll

    @property
    def contact(self):
        return self._contact
