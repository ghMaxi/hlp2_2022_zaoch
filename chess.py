import tkinter
from constants import *
from images import images
from PIL import ImageTk


class ChessApplication(tkinter.Tk):
    def __init__(self, board):
        super().__init__()

        # инициализация данных
        self.board = board
        self.images = {
            key: ImageTk.PhotoImage(
                images[key].resize( (100, 100) ))
            for key in images
        }

        # инициализация интерфейсов
        self.vars = {
            'row1': tkinter.IntVar(),
            'row2': tkinter.IntVar(),
            'col1': tkinter.IntVar(),
            'col2': tkinter.IntVar()}
        self.canvas = tkinter.Canvas(
            self,
            width=800, height=800,
            bg='brown')
        self.canvas.pack()
        self.field_row1 = tkinter.Entry(
            self, textvariable=self.vars['row1'])
        self.field_row1.pack()
        self.field_row2 = tkinter.Entry(
            self, textvariable=self.vars['row2'])
        self.field_row2.pack()
        self.field_col1 = tkinter.Entry(
            self, textvariable=self.vars['col1'])
        self.field_col1.pack()
        self.field_col2 = tkinter.Entry(
            self, textvariable=self.vars['col2'])
        self.field_col2.pack()
        self.move_button = tkinter.Button(
            self, text='Сделать ход!')
        self.move_button.pack()

        self.draw()

    def draw(self):
        high_y = 0
        colors = ('#420', '#f80')
        for row_id, row in enumerate(self.board.cells):
            low_y = high_y
            high_y += 100
            high_x = 0
            color_id = row_id % 2
            for figure in row:
                low_x = high_x
                high_x += 100
                self.canvas.create_rectangle(
                    low_x, low_y, high_x, high_y,
                    fill=colors[color_id], outline=colors[color_id])
                color_id = (color_id + 1) % 2
                if figure:
                    self.draw_figure(low_x, low_y, figure.id)

    def draw_figure(self, x, y, figure_id):
        self.canvas.create_image(
            x, y, anchor='nw',
            image=self.images[figure_id])
