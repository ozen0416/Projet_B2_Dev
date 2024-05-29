from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout, QPushButton, QFrame, QStyleOption, QStyle
from PySide6.QtCore import Qt
from typing import Optional

from ..custom import FramelessWidget


class Grid(QWidget):
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
        self.layout().setSpacing(0)

    def init_grid_button(self):
        """
        Initiate grid of buttons
        """
        for i in range(10):
            for j in range(10):
                #button = QPushButton(str(i)+str(j))
                button = DummyWidget(j, i, self)
                button.setFixedSize(40, 40)
                self.layout().addWidget(button, j, i)
                self.layout().setContentsMargins(0, 0, 0, 0)
                self.buttons.append(button)


class GridContainer(QWidget):
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


class DummyWidget(QWidget):
    """
    Dummy class as a placeholder for the game grid.
    This is just a widget with a label in its center
    """
    def __init__(self, x: int, y: int, parent=None):
        super().__init__(parent)

        self.label = QLabel(str(x)+str(y), self)
        self._x = x
        self._y = y
        self.init_layout()
        self.init_widgets()
        self.setObjectName("dummy")

    # paintEvent is overriden to make sure we can change background
    # color of custom widgets
    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)

    """
    Event that shows coordinates of where the mouse presses
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("je clique sur", self._x, self._y)
        return super().mousePressEvent(event)

    def init_layout(self):
        QVBoxLayout(self)

    def init_widgets(self):
        self.layout().addWidget(self.label, Qt.AlignCenter)
