class Message:
    def __init__(self, sender, content):
        self._sender = sender
        self._content = content

    @property
    def sender(self):
        return self._sender

    @property
    def content(self):
        return self._content


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, size: int, start_cell: Cell, cells: list):
        self.size = size
        self.start_cell = start_cell
        self.cells = cells

    def to_dict(self) -> dict:
        data = {
            "_size": self.size,
            "_pos": {"_pos": {"_x": self.cells[0].x, "_y": self.cells[0].y}},
            "_ship_cells": []
        }
        for cell in self.cells:
            data["_ship_cells"].append({"_pos": {"_x": cell.x, "_y": cell.y}})

        return data
