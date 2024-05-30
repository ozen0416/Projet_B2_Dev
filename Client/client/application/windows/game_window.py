from typing import Optional

from PySide6.QtWidgets import QApplication, QGridLayout, QWidget

from ...dataclasses import Message
from ..widgets import GridContainer, ChatWidget, BattleshipWindow


class GameWindow(BattleshipWindow):
    """
    Window of the game.
    Displays players' grids, a chat and the history of past moves
    """
    def __init__(self, contact: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.grid_enemy = GridContainer("Enemy", self)
        self.grid_ally = GridContainer("Ally", self)
        self.chat_widget = ChatWidget(contact, self)
        
        self.battleship_widget = DisplayShipContainer(self)
        self.setWindowTitle("Battleships")

        self.init_layout()
        self.init_widgets()

    def receive_message(self, data: dict):
        message = Message(data["nickname"], data["data"]["content"])
        self.chat_widget.chat_scroll.add_textbox_from_message(message)

    def init_layout(self):
        QGridLayout(self)

    def init_widgets(self):
        self.layout().addWidget(self.grid_enemy, 0, 0, 1, 1)
        self.layout().addWidget(self.grid_ally, 1, 0, 1, 1)
        self.layout().addWidget(self.battleship_widget, 0, 1, 2, 1)
        self.layout().addWidget(self.chat_widget, 0, 2, 2, 1)

