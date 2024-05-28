from PySide6.QtWidgets import QWidget, QVBoxLayout, QAbstractSlider, QApplication, QGridLayout

from .chat_textbox_widget import ChatTextbox


class ChatArea(QWidget):
    def __init__(self, contact, parent=None):
        super().__init__(parent)
        self._contact = contact

        self._textboxes = set()
        self._layout = QVBoxLayout()

        self.init_layout()

    def init_layout(self):
        self._layout.setSpacing(5)
        self._layout.addStretch(1)
        self._layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(self._layout)

    def add_textbox_from_message(self, message):
        textbox = ChatTextbox.from_message(message, self)
        self._add_textbox(textbox)

    def _add_textbox(self, textbox):
        if textbox.parent() is None:
            textbox.setParent(self)

        self._textboxes.add(textbox)
        self._layout.addWidget(textbox)

    def resizeEvent(self, event):
        scroll_bar = self.parent().parent().verticalScrollBar()
        maximum = scroll_bar.maximum()
        window = QApplication.instance().activeWindow()
        if window is None:
            return

        delta = QApplication.instance().activeWindow().height()
        if maximum - delta <= scroll_bar.sliderPosition() <= maximum + delta:
            scroll_bar.triggerAction(QAbstractSlider.SliderToMaximum)
        super().resizeEvent(event)

    @property
    def contact(self):
        return self._contact
