from score_sheet import ScoreSheet
from game_controller import GameController

score_file_name = "score.txt"
s = ScoreSheet(score_file_name)


def test_constructor():
    gc = GameController(100, 100, 50, s)
    assert gc.WIDTH == 100
    assert gc.HEIGHT == 100
    assert gc.cell == 50
    assert gc. total_col == 2
    assert gc.total_row == 2
    assert gc.player_wins is False
    gc.player_wins = True
    assert gc.player_wins is True
    assert gc.computer_wins is False
    gc.computer_wins = True
    assert gc.computer_wins is True
    assert gc.tie is False
    gc.tie = True
    assert gc.tie is True
    assert gc.score_recorded is False
    gc.score_recorded = True
    assert gc.score_recorded is True
    assert gc.score_sheet is s
    assert gc.is_over is False
    gc.is_over = True
    assert gc.is_over is True


def test_input_name():
    gc = GameController(100, 100, 50, s)
    gc.input_name("Mulan")
    assert gc.name == "Mulan"


def test_record_score():
    gc = GameController(100, 100, 50, s)
    gc.record_score(("Mulan", 6))
    assert gc.score_recorded is True


def test_game_stop():
    gc = GameController(400, 400, 100, s)
    gc.game_stop(10, 6, 16)
    assert gc.computer_wins is True
    assert gc.player_wins is False
    assert gc.is_over is True
    gc1 = GameController(400, 400, 100, s)
    gc1.is_over = True
    gc1.game_stop(6, 9, 15)
    assert gc1.computer_wins is False
    assert gc1.player_wins is True
    assert gc1.is_over is True
    gc2 = GameController(400, 400, 100, s)
    gc2.game_stop(6, 10, 16)
    assert gc2.computer_wins is False
    assert gc2.player_wins is True
    assert gc2.is_over is True
    gc3 = GameController(400, 400, 100, s)
    gc3.game_stop(8, 8, 16)
    assert gc3.computer_wins is False
    assert gc3.player_wins is False
    assert gc3.tie is True
    assert gc1.is_over is True
    gc4 = GameController(400, 400, 100, s)
    gc4.is_over = True
    gc4.game_stop(10, 3, 13)
    assert gc4.computer_wins is True
    assert gc4.player_wins is False
    assert gc4.tie is False
    assert gc4.is_over is True
    gc5 = GameController(400, 400, 100, s)
    gc5.is_over = True
    gc5.game_stop(6, 6, 12)
    assert gc5.computer_wins is False
    assert gc5.player_wins is False
    assert gc5.tie is True
    assert gc5.is_over is True

# Not able to test gc.update since it displays texts.
