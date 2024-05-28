from ..custom import ScalingTextEdit


class ChatMessageText(ScalingTextEdit):
    def __init__(self, content, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('ChatMessageText')

        self.setReadOnly(True)
        self.setPlainText(content)
