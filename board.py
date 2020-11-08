class Board:
    """This class represent the board, meaning drawing black
    lines to show each cell."""
    def __init__(self, WIDTH, HEIGHT, CELL, d):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CELL = CELL
        self.disk = d

    def display(self):
        """Draw the line on the board
        NONE -> NONE"""
        stroke_color = 0
        stroke_weight = 3
        stroke(stroke_color)
        strokeWeight(stroke_weight)
        line_start_coordinate = 0
        for i in range(self.WIDTH // self.CELL - 1):
            line(i * self.CELL + self.CELL, line_start_coordinate,
                 i * self.CELL + self.CELL, self.HEIGHT)
        for i in range(self.HEIGHT // self.CELL - 1):
            line(line_start_coordinate, i * self.CELL + self.CELL, self.WIDTH,
                 i * self.CELL + self.CELL)
        self.disk.check_legal(True)
        print("Player starts!")
