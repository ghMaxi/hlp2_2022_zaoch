from queen import Queen
from king import King
from rook import Rook
from constants import *
WIDTH = 8
HEIGHT = 8


class Board:
    def __init__(self):
        self.cells = [[None] * WIDTH for _ in range(HEIGHT)]
        self.cells[0][0] = Rook(BLACK)
        self.cells[0][3] = Queen(BLACK)
        self.cells[0][4] = King(BLACK)
        self.cells[7][3] = Queen(WHITE)
        self.cells[7][4] = King(WHITE)


if __name__ == "__main__":
    board = Board()
    for row_id, row in enumerate(board.cells):
        for col_id, figure in enumerate(row):
            print(row_id, col_id, figure)
