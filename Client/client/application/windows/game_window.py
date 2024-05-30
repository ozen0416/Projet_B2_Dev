from typing import Optional

from PySide6.QtWidgets import QApplication, QGridLayout, QWidget, QLabel

from ...dataclasses import Message
from ..widgets import GridContainer, ChatWidget, BattleshipWindow, DisplayShipContainer
from ...tools import GridCellState, GameState


class GameWindow(BattleshipWindow):
    """
    Window of the game.
    Displays players' grids, a chat and the history of past moves

    Whenever a ship is placed, all the ships check if it was them
    that was placed, if so, decrement the count of ships
    """
    def __init__(self, contact: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.game_state_label = QLabel(self)
        self.game_state = None
        self.update_state(GameState.PLACEMENT)

        self.grid_enemy = GridContainer("Enemy", self)
        self.grid_ally = GridContainer("Ally", self, True)
        self.chat_widget = ChatWidget(contact, self)


        self.battleship_widget = DisplayShipContainer(self)

        self.setWindowTitle("Battleships")

        self.init_layout()
        self.init_widgets()

    def update_state(self, game_state: GameState):
        self.game_state = game_state
        if self.game_state == GameState.WAITING:
            self.game_state_label.setText("WAITING")
        elif self.game_state == GameState.PROGRESS or self.game_state == GameState.PLACEMENT:
            self.game_state_label.setText("YOUR MOVE")
        else:
            self.game_state_label.setText("FINISHED")

    def update_enemy_grid(self, data: dict):
        status = data["status"]
        status = 1 if status >= 2 else status
        self.grid_enemy.grid.update_grid_state(data["_pos"]["_x"], data["_pos"]["_y"], GridCellState(status))

    def update_ally_grid(self, data: dict):
        status = data["status"]
        status = 1 if status >= 2 else status
        self.grid_ally.grid.update_grid_state(data["_pos"]["_x"], data["_pos"]["_y"], GridCellState(status))

    def receive_message(self, data: dict):
        message = Message(data["nickname"], data["data"]["content"])
        self.chat_widget.chat_scroll.add_textbox_from_message(message)

    def start_game(self, request: dict):
        if request["data"]["start"]:
            self.update_state(GameState.PROGRESS)
        else:
            self.update_state(GameState.WAITING)

    def send_hit(self):
        if self.game_state != GameState.PROGRESS:
            return
        if self.grid_enemy.grid.waiting_cell is None:
            return

        cell_x = self.grid_enemy.grid.waiting_cell._x
        cell_y = self.grid_enemy.grid.waiting_cell._y
        data_hit = {
            "request": ["GAME", "HIT"],
            "data": {"_pos": {"_x": cell_x, "_y": cell_y}}
        }
        QApplication.instance().send_request(data_hit)

    def send_placement(self):
        if self.game_state != GameState.PLACEMENT:
            return

        ships = self.grid_ally.get_placement()
        if len(ships) != 5:
            return

        data_placement = {
            "request": ["GAME", "PLACEMENT"],
            "data": {"_ships": ships}
        }
        print(data_placement)
        QApplication.instance().send_request(data_placement)
        self.update_state(GameState.WAITING)

    def init_layout(self):
        QGridLayout(self)

    def init_widgets(self):
        # Confirm Button Signals
        self.battleship_widget.button.clicked.connect(self.send_placement)
        self.battleship_widget.button.clicked.connect(self.send_hit)

        # Decrement ship count on signal
        for ship in self.battleship_widget.ships:
            self.grid_ally.grid.ship_dropped.connect(ship.use_ship)

        self.layout().addWidget(self.game_state_label, 0, 0, 1, 3)
        self.layout().addWidget(self.grid_enemy, 1, 0, 1, 1)
        self.layout().addWidget(self.grid_ally, 2, 0, 1, 1)
        self.layout().addWidget(self.battleship_widget, 1, 1, 2, 1)
        self.layout().addWidget(self.chat_widget, 1, 2, 2, 1)


