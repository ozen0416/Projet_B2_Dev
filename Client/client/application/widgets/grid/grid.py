from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout, QPushButton
from PySide6.QtCore import Qt
from typing import Optional

from ..customs import FramelessWidget


class Grid(FramelessWidget):
    """
    Widget that instantiate a grid of widgets
    """
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.buttons = []
        
        self.init_layout()
        self.init_grid_button()

    def init_layout(self):
        QGridLayout(self)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def init_grid_button(self):
        for i in range(10):
            for j in range(10):
                #button = QPushButton(str(i)+str(j))
                button = DummyWidget(str(i)+str(j), self)
                button.setFixedSize(40, 40)
                self.layout().addWidget(button, i, j)
                self.buttons.append(button)


class GridContainer(FramelessWidget):
    """
    Container of the two grids that serve as maps
    """
    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        self.label = QLabel(title, self)
        self.grid = Grid(self)

        self.init_layout()
        self.init_widgets()

    def init_layout(self):
        QVBoxLayout(self)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def init_widgets(self):
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.grid)


class DummyWidget(FramelessWidget):
    """
    Dummy class as a placeholder for the game grid.
    This is just a widget with a label in its center
    """
    def __init__(self, title: str, parent=None):
        super().__init__(parent)

        self.label = QLabel(title, self)

        self.init_layout()
        self.init_widgets()
    
    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.layout().addWidget(self.label, Qt.AlignCenter)
