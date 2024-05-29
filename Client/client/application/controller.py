from .windows import HomeWindow, GameWindow

WINDOW_TYPES = [
    'home',
    'game',
    ]


class Controller:
    def __init__(self):
        self.current_window = None
        self.home_window = None
        self.game_window = None
        self.switch_emitted("home")

    def show_game(self):
        self.game_window = GameWindow()
        self.game_window.switch_window.connect(self.switch_emitted)
        self.current_window = self.game_window

    def show_home(self):
        self.home_window = HomeWindow()
        self.home_window.switch_window.connect(self.switch_emitted)
        self.current_window = self.home_window

    def switch_emitted(self, window_type):
        print(f"SWITCH EMITTED: {window_type}")
        window_type = window_type.lower()

        if window_type not in WINDOW_TYPES:
            return
        if self.current_window is not None:
            self.current_window.close()

        if window_type == 'home':
            self.show_home()
        elif window_type == 'game':
            self.show_game()

        self.current_window.show()
