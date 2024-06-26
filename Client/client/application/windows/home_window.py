from typing import Optional

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QHBoxLayout, QSizePolicy, QWidget, QLabel, QVBoxLayout, QGridLayout

from ..widgets import SearchGame, Login, BattleshipWindow


class HomeWindow(BattleshipWindow):
    """
    Home window before a game is played.

    It is here you can change username, search for a game
    and see your history of matches.
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.left_widget = ContainerWidget(self)

        self.setWindowTitle("Battleships")

        self.init_layout()
        self.init_widget()

    def init_layout(self):
        QGridLayout(self)

    def init_widget(self):
        self.layout().addWidget(self.left_widget)


class ContainerWidget(QWidget):
    """
    Class to group the SearchGame and the UserInput
    in a single widget
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.play_button = SearchGame(self)
        self.login = Login(self)

        self.init_layout()
        self.init_widget()

    def init_layout(self):
        QVBoxLayout(self)

    def init_widget(self):
        self.layout().addWidget(self.login)
        self.layout().addWidget(self.play_button)

        self.login.setMaximumSize(300, 200)  # width, height
        self.play_button.setMaximumSize(500, 200)  # width, height
        #self.login.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)  # width, height
        #self.login.move(50, 50)  # width, height
        #self.login.resize(300, 200)  # width, height
