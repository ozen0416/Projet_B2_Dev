from typing import Optional

from PySide6.QtWidgets import QHBoxLayout, QWidget, QLabel, QVBoxLayout

from ..widgets import FramelessWidget
from ..widgets import SearchGame
from ..widgets import Login 


class HomeWindow(FramelessWidget):
    """
    Home window before a game is played.

    It is here you can change username, search for a game
    and see your history of matches.
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        
        #self.timer = SearchGame(self)
        self.left_widget = ContainerWidget(self)
        self.label_test = QLabel("feurhahahaha", self)

        self.setWindowTitle("Battleships")

        self.init_layout()
        self.init_widget()

    def init_layout(self):
        QHBoxLayout(self)

    def init_widget(self):
        self.layout().addWidget(self.left_widget)
        self.layout().addWidget(self.label_test)


class ContainerWidget(FramelessWidget):
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


