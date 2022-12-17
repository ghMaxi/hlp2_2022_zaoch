class Figure:
    symbol = '@'

    def __init__(self, side):
        self.side = side

    @property
    def id(self):
        return self.side + self.symbol
