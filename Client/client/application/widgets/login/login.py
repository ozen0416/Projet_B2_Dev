from PySide6.QtWidgets import QLineEdit, QLabel, QVBoxLayout, QPushButton

from ..customs import FramelessWidget

class Login(FramelessWidget):
    """
    Login widget with two inputs, the username and the password
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.submit = QPushButton("Submit", self)

        self.label_username = QLabel("Username", self)
        self.label_password = QLabel("Password", self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.password.setEchoMode(QLineEdit.Password)

        self.submit.clicked.connect(self.get_cred)

        self.layout().addWidget(self.label_username)
        self.layout().addWidget(self.username)
        self.layout().addWidget(self.label_password)
        self.layout().addWidget(self.password)
        self.layout().addWidget(self.submit)
        
    def get_cred(self):
        print(self.username.text())
        print(self.password.text())
