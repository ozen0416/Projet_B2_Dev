from typing import Optional

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
from PySide6.QtCore import QTime, QTimer

from ....tools import ButtonState


class SearchGame(QWidget):
    """
    Widget to search for a game or cancel the search.

    Shows the time that has past since the beginning of the search.
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.start_time = None
        self.button_state = ButtonState.PLAY

        self.play = QPushButton("Start", self)
        self.label = QLabel("PLAY", self)
        self.timer = QTimer(self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.play.clicked.connect(self.button_handler)
        self.timer.timeout.connect(self.update_time)

        self.layout().addWidget(self.label)
        self.layout().addWidget(self.play)

    def button_handler(self):
        if self.button_state == ButtonState.PLAY:
            matchmaking_in_data = {
                "request": ["MATCHMAKING", "IN"],
            }
            QApplication.instance().send_request(matchmaking_in_data)
            self.start_timer()
        else:
            matchmaking_out_data = {
                "request": ["MATCHMAKING", "OUT"],
            }
            QApplication.instance().send_request(matchmaking_out_data)
            self.cancel_play()

    def start_timer(self):
        """
        Method that will be called each time the PlayButton is clicked
        and its state is PLAY

        Calls for a matchmaking request and wait for a response
        """
        self.start_time = QTime.currentTime()
        self.timer.start(1000)
        self.play.setText("CANCEL")
        self.label.setText("Time passed: 0")
        self.button_state = ButtonState.CANCEL

    def cancel_play(self):
        """
        Method that will be called each time the PlayButton is clicked
        and its state is CANCEL

        Cancels the matchmaking request
        """
        self.timer.stop()
        self.label.setText("PLAY")
        self.play.setText("PLAY")
        self.button_state = ButtonState.PLAY

    def update_time(self):
        """
        Method that will be called each time the timer finishes.
        By default the timer finishes in one second.
        """
        elapsed_time = self.start_time.secsTo(QTime.currentTime())

        self.label.setText(f"Time passed: {elapsed_time}")
