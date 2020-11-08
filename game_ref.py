import time
import random


class GameRef:
    """This class controls the turn in the game."""
    def __init__(self, game_controller, CELL):
        self.player_turn = True
        self.gc = game_controller
        self.cell = CELL

    def player_move(self, x, y, disks):
        """Make sure player is placing the tile in a legal spot, or switch
        turns if there is no more legal moves, or stop the game.
        INT, INT, OBJECT -> NONE"""
        if self.player_turn and disks.legal_table:
            disks.player_update(x, y)
        else:
            # When there are no more legal moves for black, check legal moves for white. If there are legal moves, change turn the white. End the game otherwise.
            disks.check_legal(False)
            if disks.legal_table:
                self.player_turn = False
            else:
                print("No more move!")
                self.gc.is_over = True
        white_score = disks.white_score
        black_score = disks.black_score
        total_count = disks.total_count
        self.gc.update(white_score, black_score, total_count)

    def computer_move(self, disks):
        """Make sure computer is placing the tile in a legal spot, or switch
        turns if there is no more legal moves, or stop the game.
        OBJECT -> NONE"""
        sleep_time = 0.6
        time.sleep(sleep_time)
        white_score = disks.white_score
        black_score = disks.black_score
        total_count = disks.total_count
        if disks.legal_table:
            coordinate = random.choice(tuple(disks.legal_table))
            disks.computer_update(coordinate[1] * self.cell,
                                  coordinate[0] * self.cell)
            self.gc.update(white_score, black_score, total_count)
            if not disks.legal_table:
                disks.check_legal(False)
                self.player_turn = False
        else:
            disks.check_legal(True)
            if disks.legal_table:
                self.player_turn = True
                print("Your turn!")
            else:
                print("No more move!")
                self.gc.is_over = True
            white_score = disks.white_score
            black_score = disks.black_score
            total_count = disks.total_count
            self.gc.update(white_score, black_score, total_count)
