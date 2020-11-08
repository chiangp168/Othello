from disk import Disk


class Disks:
    """This class represent multiple disks objects on the board."""
    def __init__(self, WIDTH, HEIGHT, CELL, gr):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.cell = CELL
        num_start_disks = 2
        self.black_score = num_start_disks
        self.white_score = num_start_disks
        self.total_count = num_start_disks * 2
        self.gr = gr
        self.total_col = self.WIDTH // self.cell
        self.total_row = self.HEIGHT // self.cell
        self.table = [[0] * self.total_col for i in range(self.total_row)]
        half_cell = self.cell / 2
        self.disk1 = (Disk(self.WIDTH // 2 + half_cell,
                      self.HEIGHT // 2 - half_cell, self.cell))
        self.disk2 = (Disk(self.WIDTH // 2 - half_cell,
                      self.HEIGHT // 2 + half_cell, self.cell))
        self.disk3 = (Disk(self.WIDTH // 2 - half_cell,
                      self.HEIGHT // 2 - half_cell, self.cell))
        self.disk4 = (Disk(self.WIDTH // 2 + half_cell,
                      self.HEIGHT // 2 + half_cell, self.cell))
        self.table[self.disk1.row][self.disk1.column] = self.disk1
        self.table[self.disk2.row][self.disk2.column] = self.disk2
        self.table[self.disk3.row][self.disk3.column] = self.disk3
        self.table[self.disk4.row][self.disk4.column] = self.disk4
        self.disk3.draw_black = False
        self.disk4.draw_black = False
        self.legal_table = set()

    def player_update(self, x, y):
        """Create and draw new tile object when player puts down a new tile.
        INT and INT -> NONE"""
        row = y // self.cell
        column = x // self.cell
        if self.table[row][column] == 0 and (row, column) in self.legal_table:
            self.black_score += 1
            self.gr.player_turn = False
            self.flip_tiles(x, y, True)
            print("Computer is thinking hard...")

    def computer_update(self, x, y):
        """Create and draw new tile object when computer puts down a new tile.
        INT and INT -> NONE"""
        self.white_score += 1
        self.gr.player_turn = True
        self.flip_tiles(x, y, False)
        print("Your turn!")

    def _flip_tiles_one_dir(self, position, dir_fn, is_black):
        """Flip tile colors in one direction.
        TUPLE, FUNCTION, BOOLEAN -> BOOLEAN"""
        row, column = position
        if not self._is_position_valid(position):
            return False
        current_disk = self.table[row][column]
        if current_disk == 0:
            return False
        if current_disk.draw_black == is_black:
            return True
        next_result = self._flip_tiles_one_dir(dir_fn(position),
                                               dir_fn, is_black)
        if next_result:
            current_disk.draw_black = is_black
            current_disk.display()
            if current_disk.draw_black:
                self.black_score += 1
                self.white_score -= 1
            else:
                self.white_score += 1
                self.black_score -= 1
        return next_result

    def flip_tiles(self, x, y, is_black):
        """Flip tile colors in all eight directions.
        INT, INT -> BOOLEAN"""
        d = Disk(x, y, self.cell)
        position = (d.row, d.column)
        self._flip_tiles_one_dir(self._move_right(position),
                                 self._move_right, is_black)
        self._flip_tiles_one_dir(self._move_left(position),
                                 self._move_left, is_black)
        self._flip_tiles_one_dir(self._move_up(position),
                                 self._move_up, is_black)
        self._flip_tiles_one_dir(self._move_down(position),
                                 self._move_down, is_black)
        self._flip_tiles_one_dir(self._move_left_up(position),
                                 self._move_left_up, is_black)
        self._flip_tiles_one_dir(self._move_left_down(position),
                                 self._move_left_down, is_black)
        self._flip_tiles_one_dir(self._move_right_up(position),
                                 self._move_right_up, is_black)
        self._flip_tiles_one_dir(self._move_right_down(position),
                                 self._move_right_down, is_black)
        d.draw_black = is_black
        d.display()
        self.table[d.row][d.column] = d
        self.total_count += 1
        self.check_legal(self.gr.player_turn)

    def _move_right(self, position):
        """Position of the right cell from current disk.
        TUPLE -> TUPLE"""
        return position[0], position[1] + 1

    def _move_left(self, position):
        """Position of the left cell from current disk.
        TUPLE -> TUPLE"""
        return position[0], position[1] - 1

    def _move_up(self, position):
        """Position of the upper cell from current disk.
        TUPLE -> TUPLE"""
        return position[0] - 1, position[1]

    def _move_down(self, position):
        """Position of the down cell from current disk.
        TUPLE -> TUPLE"""
        return position[0] + 1, position[1]

    def _move_left_up(self, position):
        """Position of the left upper cell from current disk.
        TUPLE -> TUPLE"""
        return position[0] - 1, position[1] - 1

    def _move_left_down(self, position):
        """Position of the down left cell from current disk.
        TUPLE -> TUPLE"""
        return position[0] + 1, position[1] - 1

    def _move_right_up(self, position):
        """Position of the right upper cell from current disk.
        TUPLE -> TUPLE"""
        return position[0] - 1, position[1] + 1

    def _move_right_down(self, position):
        """Position of the down right cell from current disk.
        TUPLE -> TUPLE"""
        return position[0] + 1, position[1] + 1

    def _is_position_valid(self, position):
        """Checking if the position of a cell is out of board bound.
        TUPLE -> BOOLEAN"""
        return (0 <= position[0] <= self.total_row - 1 and
                0 <= position[1] <= self.total_col - 1)

    def check_legal(self, is_black):
        """Go through each grid, and check all legals moves in 8 directions of a tile based on tile color.
        BOOLEAN -> NONE"""
        self.legal_table = set()
        for grid in self.table:
            for item in grid:
                if not item == 0:
                    if item.draw_black == is_black:
                        for row in range(item.row - 1, item.row + 2):
                            for column in range(item.column - 1,
                                                item.column + 2):
                                if (self._is_position_valid((row, column)) and
                                    not self.table[row][column] == 0 and
                                    self.table[row][column].draw_black
                                   != is_black):
                                    row_difference = row - item.row
                                    column_difference = column - item.column
                                    self.check_adjacent(row + row_difference,
                                                        column
                                                        + column_difference,
                                                        row_difference,
                                                        column_difference,
                                                        is_black)

    def check_adjacent(self, row, column, row_difference,
                       column_difference, is_black):
        """Check the next adjacent position from current position to see if
        it's a legal move position.
        INT, INT, INT, INT, BOOLEAN -> NONE"""
        if self._is_position_valid((row, column)):
            if self.table[row][column] == 0:
                coordinate = (row, column)
                self.legal_table.add(coordinate)
            elif self.table[row][column].draw_black != is_black:
                self.check_adjacent(row + row_difference, column
                                    + column_difference, row_difference,
                                    column_difference, is_black)

    def display(self):
        """Display the middle four tiles."""
        self.disk1.display()
        self.disk2.display()
        self.disk3.display()
        self.disk4.display()
