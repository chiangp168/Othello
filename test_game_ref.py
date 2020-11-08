from game_controller import GameController
from game_ref import GameRef
from score_sheet import ScoreSheet
import time
import random
from disks import Disks

score_file_name = "score.txt"
s = ScoreSheet(score_file_name)
gc = GameController(400, 400, 100, s)
gr = GameRef(gc, 100)
d = Disks(400, 400, 100, gr)


def test_constructor():
    gr1 = GameRef(gc, 100)
    assert gr1.player_turn is True
    assert gr1.gc is gc
    assert gr1.cell == 100


# Both player_move and computer_move includes methods that display drawing
# on screen, so I was not able to test for those two functions.
