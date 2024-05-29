from PySide6.QtWidgets import QLabel 
from PySide6.QtCore import QTimer, QTime


class Timer(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime()

        time_str = current_time.toString('hh:mm:ss')

        self.setText(time_str)
