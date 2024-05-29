from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy, QStyleOption, QStyle
from PySide6.QtGui import QPainter

from .chat_message_text import ChatMessageText


class ChatTextbox(QWidget):
    def __init__(self, sender: str, content: str, parent=None):
        super().__init__(parent)

        self.setObjectName('ChatTextbox')

        self._layout = QGridLayout()

        self.sender = sender
        self.content = content

        self.sender_label = QLabel(self)
        self.sender_label.setObjectName('TextboxSender')
        self.content_text = ChatMessageText(self.content, self)
        self.sizePolicy().setHorizontalPolicy(QSizePolicy.MinimumExpanding)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        self._layout.setSpacing(0)
        self.setLayout(self._layout)

    def init_widgets(self):
        self.sender_label.setText(self.sender)
        self.sender_label.setWordWrap(True)
        self.sender_label.setScaledContents(False)

        self._layout.addWidget(self.sender_label)
        self._layout.addWidget(self.content_text)

    def enterEvent(self, event):
        self.setStyleSheet('''QWidget#ChatTextbox {
                                background-color: rgba(73, 73, 73, 40);
                            }
                            QWidget#ChatTextbox * {
                                background-color: transparent;
                            }''')

        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet('')
        super().leaveEvent(event)

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)

        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        super().paintEvent(event)

    @classmethod
    def from_message(cls, message, parent=None):
        self = cls(
            message.sender,
            message.content,
            parent
        )

        return self
