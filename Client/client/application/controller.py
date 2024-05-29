from .windows import HomeWindow, GameWindow

WINDOW_TYPES = [
    'login',
    'register',
    'master',
    ]


class Controller:
    def __init__(self):
        self.home_window = HomeWindow()
        self.home_window.switch_window.connect(self.switch_emitted)
        self.master_window = None
        self.current_window = self.login_window

    def show_login(self):
        self.current_window = self.login_window

    def show_register(self):
        self.current_window = self.register_window

    def show_master(self):
        self.master_window = MasterWindow()
        self.master_window.switch_window.connect(self.switch_emitted)
        self.current_window = self.master_window

    def switch_emitted(self, window_type):
        window_type = window_type.lower()

        if window_type not in WINDOW_TYPES:
            return

        self.current_window.close()

        if window_type == 'master':
            self.show_master()
        if window_type == 'login':
            self.show_login()
        elif window_type == 'register':
            self.show_register()

        self.current_window.show()
