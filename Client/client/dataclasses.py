class Message:
    def __init__(self, sender, content):
        self._sender = sender
        self._content = content

    @property
    def sender(self):
        return self._sender

    @property
    def content(self):
        return self._content
