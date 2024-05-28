from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextOption
from PySide6.QtCore import Qt


class ScalingTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        self.min_height = 0
        self.max_height = 65000
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def line_count(self):
        max_width = self.width()
        if self.verticalScrollBar() and self.verticalScrollBar().isVisible():
            max_width -= self.verticalScrollBar().width()

        parent = self.parent()
        while parent is not None:
            if hasattr(parent, 'verticalScrollBar'):
                max_width -= parent.verticalScrollBar().width()
            parent = parent.parent()

        formatted_lines = []
        current_line = ""
        lines = self.toPlainText().splitlines(keepends=True)

        words = []
        for line in lines:
            words.extend(line.split(' '))

        while len(words) > 0:
            word = words.pop(0)
            current_line_width = self.fontMetrics().boundingRect(current_line).width()
            word_width = self.fontMetrics().boundingRect(word).width()

            if current_line_width + word_width < max_width:
                current_line += ' ' + word
                if '\n' in word:
                    formatted_lines.append(current_line.strip())
                    current_line = ""
            elif current_line_width + word_width >= max_width:
                if current_line == "":
                    built = ''
                    for letter in word:
                        if self.fontMetrics().boundingRect(built + letter).width() > max_width:
                            break
                        built += letter
                    current_line += word[:len(built)]
                    words.insert(0, word[len(built):])
                else:
                    words.insert(0, word)
                formatted_lines.append(current_line.strip())
                current_line = ""

        formatted_lines.append(current_line.strip())
        return len(formatted_lines)

    def resizeEvent(self, event):
        height = self.line_count() * self.fontMetrics().height() + 10
        if height > self.max_height:
            height = self.max_height
        elif height < self.min_height:
            height = self.min_height

        self.setFixedHeight(height)

        super().resizeEvent(event)
