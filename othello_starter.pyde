# Run with Processing Application
from board import Board
from disks import Disks
from game_controller import GameController
from game_ref import GameRef
from score_sheet import ScoreSheet

# Create the size of the screen, and the size of each cell.
WIDTH = 800
HEIGHT = WIDTH
CELL = 100
score_file_name = "score.txt"
s = ScoreSheet(score_file_name)
gc = GameController(WIDTH, HEIGHT, CELL, s)
gr = GameRef(gc, CELL)
d = Disks(WIDTH, HEIGHT, CELL, gr)
b = Board(WIDTH, HEIGHT, CELL, d)


def setup():
    """Display things that only need to be drawn once."""
    answer = _input('Enter your game name')
    size(WIDTH, HEIGHT)
    colorMode(RGB, 100)
    background(20, 60, 40)
    b.display()
    d.display()
    gc.input_name(answer)


def _input(self, message=''):
    """In order for users to enter their names."""
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    """Redraw and update the screen."""
    if not gr.player_turn and not gc.is_over:
        gr.computer_move(d)


def mousePressed():
    """Draw where the user clicked."""
    if gr.player_turn and not gc.is_over:
        gr.player_move(mouseX, mouseY, d)
