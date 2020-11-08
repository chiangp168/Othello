from board import Board
from disks import Disks
from game_controller import GameController
from game_ref import GameRef
from score_sheet import ScoreSheet


def test_constructor():
    """Test constructor"""
    score_file_name = "score.txt"
    s = ScoreSheet(score_file_name)
    gc = GameController(600, 400, 50, s)
    gr = GameRef(gc, 100)
    d = Disks(600, 400, 50, gr)
    b = Board(600, 400, 50, d)
    assert b.WIDTH == 600
    assert b.HEIGHT == 400
    assert b.CELL == 50
    assert b.disk is d
