class Disk:
    """This class represent one disk tile."""
    def __init__(self, x, y, cell):
        self.x = x
        self.y = y
        self.CELL = cell
        self.draw_black = True
        self.column = int(self.x // self.CELL)
        self.row = int(self.y // self.CELL)

    def display(self):
        """Draw either black or white tile depending on the boolean value.
        NONE -> NONE"""
        color_black = 0
        color_white = 100
        cell_disk_size_diff = 10
        if self.draw_black:
            fill(color_black)
        else:
            fill(color_white)
        ellipse(self.column * self.CELL + self.CELL / 2,
                self.row * self.CELL + self.CELL / 2,
                self.CELL - cell_disk_size_diff,
                self.CELL - cell_disk_size_diff)

    def __repr__(self):
        """String representation of a disk object."""
        if self.draw_black:
            return "Black"
        else:
            return "White"
