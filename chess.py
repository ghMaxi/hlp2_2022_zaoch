import tkinter
from constants import *
from images import get_raw_images
from PIL import ImageTk


class ChessApplication(tkinter.Tk):
    def __init__(self, board):
        super().__init__()

        # инициализация данных
        self.board = board
        images = get_raw_images()
        self.images = {
            key: ImageTk.PhotoImage(
                images[key].resize( (100, 100) ))
            for key in images
        }

        # инициализация интерфейсов
        self.vars = {
            'row1': tkinter.IntVar(),
            'row2': tkinter.IntVar(),
            'col1': tkinter.StringVar(),
            'col2': tkinter.StringVar(),
            'msg': tkinter.StringVar(value='Сделайте ход!')}
        self.canvas = tkinter.Canvas(
            self,
            width=800, height=800,
            bg='brown')
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.saved_click = None
        self.canvas.pack()
        tkinter.Label(self, textvariable=self.vars['msg']).pack(side="right")
        tkinter.Entry(self, textvariable=self.vars['col1']).pack()
        tkinter.Entry(self, textvariable=self.vars['row1']).pack()
        tkinter.Entry(self, textvariable=self.vars['col2']).pack()
        tkinter.Entry(self, textvariable=self.vars['row2']).pack()
        tkinter.Button(self, text='Сделать ход!',
                       command=self.text_move).pack()
        self.draw()

    def mouse_click(self, event):
        if self.saved_click:
            new_click = event.x // 100, event.y // 100
            self.make_move(
                self.saved_click[1], self.saved_click[0],
                new_click[1], new_click[0])
            self.saved_click = None
        else:
            self.saved_click = event.x // 100, event.y // 100
            if not self.board.cells[self.saved_click[1]][self.saved_click[0]]:
                self.saved_click = None
        self.draw()
    
    def make_move(self, start_row, start_col, end_row, end_col):
        result = self.board.make_move(
            start_row, start_col, end_row, end_col)
        self.vars['msg'].set(result if result else "Сделайте ход!")

    def text_move(self):
        start_row = 8 - self.vars['row1'].get()
        start_col = 'abcdefgh'.index(self.vars['col1'].get())
        end_row = 8 - self.vars['row2'].get()
        end_col = 'abcdefgh'.index(self.vars['col2'].get())
        self.make_move(start_row, start_col, end_row, end_col)
        self.draw()
    
    def draw(self):
        high_y = 0
        colors = ('#420', '#f80')
        for row_id, row in enumerate(self.board.cells):
            low_y = high_y
            high_y += 100
            high_x = 0
            color_id = row_id % 2
            for col_id, figure in enumerate(row):
                low_x = high_x
                high_x += 100
                if (self.saved_click and col_id == self.saved_click[0] and
                                row_id == self.saved_click[1]):
                    outline_color = '#0f0'
                else:
                    outline_color = colors[color_id]
                self.canvas.create_rectangle(
                    low_x, low_y, high_x, high_y,
                    fill=colors[color_id], outline=outline_color)
                color_id = (color_id + 1) % 2
                if figure:
                    self.draw_figure(low_x, low_y, figure.id)

    def draw_figure(self, x, y, figure_id):
        self.canvas.create_image(
            x, y, anchor='nw',
            image=self.images[figure_id])


def main():
    from board import Board
    ChessApplication(Board.start()).mainloop()


if __name__ == "__main__":
    main()
    
