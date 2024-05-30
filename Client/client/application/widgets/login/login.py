from PySide6.QtWidgets import QLineEdit, QLabel, QPushButton, QWidget, QFormLayout, QApplication


class Login(QWidget):
    """
    Login widget with two inputs, the username and the password
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.lineedit_username = QLineEdit(self)
        self.lineedit_id = QLineEdit(self)

        self.label_username = QLabel("Username", self)
        self.label_id = QLabel("ID", self)
        self.submit = QPushButton("Submit", self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QFormLayout(self)

    def init_widgets(self):
        # self.lineedit_id.setEchoMode(QLineEdit.Password)
        self.lineedit_username.setText(QApplication.instance().user)
        self.lineedit_id.setText(QApplication.instance().client_id)

        self.submit.clicked.connect(self.get_cred)

        self.layout().addRow(self.label_username, self.lineedit_username)
        self.layout().addRow(self.label_id, self.lineedit_id)
        self.layout().addRow(self.submit)

    def get_cred(self):
        QApplication.instance().user = self.lineedit_username.text()
        QApplication.instance().client_id = self.lineedit_id.text()
        QApplication.instance().save_settings()
