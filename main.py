from board import Board
from chess import ChessApplication
board = Board()
app = ChessApplication(board)

if __name__ == "__main__":
    app.mainloop()
