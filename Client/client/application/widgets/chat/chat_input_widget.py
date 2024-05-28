from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, Signal, Slot
from ..custom import ScalingTextEdit

from ....dataclasses import Message


class ChatInputWidget(ScalingTextEdit):
    return_pressed = Signal()

    def __init__(self, contact, parent=None):
        super().__init__(parent=parent)

        self.setPlaceholderText(f'Message @{contact}')

        self.return_pressed.connect(self.send_message)
        self.max_height = self.fontMetrics().height() * 5 + 10
        self.min_height = self.fontMetrics().height() + 10

    @Slot()
    def send_message(self):
        content = self.toPlainText().strip('\r\n ')
        if content == '' or len(content) > 2000:
            return

        message = Message(QApplication.instance().user, content)
        self.setText('')
        chat_scroll = self.parent().chat_scroll
        chat_scroll.add_textbox_from_message(message)

    def keyPressEvent(self, event):
        combination = event.keyCombination()
        if combination.keyboardModifiers() == Qt.ShiftModifier and combination.key() == Qt.Key_Return:
            self.insertPlainText('\n')
            return

        if event.key() == Qt.Key_Return:
            self.return_pressed.emit()
            return

        super().keyPressEvent(event)
