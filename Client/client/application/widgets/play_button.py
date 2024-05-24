from typing import Optional

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QTime, QTimer

from .client.tools import ButtonState # trop chiant

class SearchGame(QWidget):
    """
    Widget to search for a game or cancel the search.

    Shows the time that has past since the beginning of the search.
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.start_time = None

        self.button_state = "feur"

        self.play = QPushButton("Start", self)
        self.label = QLabel("Elapsed time: 0", self)
        self.timer = QTimer(self)

        self.play.clicked.connect(self.start_timer)
        self.timer.timeout.connect(self.update_time)

        self.init_layout()
        self.init_widgets()


    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.play)

    def start_timer(self):
        self.start_time = QTime.currentTime()
        self.timer.start(1000)

    def update_time(self):
        elapsed_time = self.start_time.secsTo(QTime.currentTime())

        self.label.setText(f"Time passed: {elapsed_time}")
