from queen import Queen
from king import King
from rook import Rook
from bishop import Bishop
from pawn import Pawn
from horse import Horse
from constants import *
WIDTH = 8
HEIGHT = 8


class Board:
    @classmethod
    def start(cls):
        cells = [[None] * WIDTH for _ in range(HEIGHT)]
        for figs, pawns, side in (0, 1, BLACK), (7, 6, WHITE):
            cells[figs][0] = Rook(side)
            cells[figs][7] = Rook(side)
            cells[figs][1] = Horse(side)
            cells[figs][6] = Horse(side)
            cells[figs][2] = Bishop(side)
            cells[figs][5] = Bishop(side)
            cells[figs][3] = Queen(side)
            cells[figs][4] = King(side)
            for col in range(WIDTH):
                cells[pawns][col] = Pawn(side)
        return cls(cells)

    def __init__(self, cells):
        self.cells = cells


if __name__ == "__main__":
    board = Board()
    for row_id, row in enumerate(board.cells):
        for col_id, figure in enumerate(row):
            print(row_id, col_id, figure)
