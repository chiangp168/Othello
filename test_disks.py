from disk import Disk
from disks import Disks
from game_controller import GameController
from game_ref import GameRef
from score_sheet import ScoreSheet

score_file_name = "score.txt"
s = ScoreSheet(score_file_name)
gc = GameController(100, 100, 50, s)
gr = GameRef(gc, 100)


def test_constructor():
    """Test constructor"""
    d = Disks(100, 100, 50, gr)
    assert d.WIDTH == 100
    assert d.HEIGHT == 100
    assert d.cell == 50
    num_start_disks = 4
    assert d.black_score == 2
    assert d.white_score == 2
    assert d.total_count == 4
    assert d.gr is gr
    assert d.total_col == 2
    assert d.total_row == 2
    assert d.table == [[d.disk3, d.disk1], [d.disk2, d.disk4]]
    half_cell = d.cell / 2
    assert half_cell == 25
    assert repr(d.disk1) == "Black"
    assert repr(d.disk2) == "Black"
    assert repr(d.disk3) == "White"
    assert repr(d.disk4) == "White"
    assert d.disk3.draw_black is False
    assert d.disk4.draw_black is False
    assert d.legal_table == set()

    # For player_update, computer_update, method, it calls the flip_tiles
    # method which calls on _flip_tiles_one_dir that contains display graph.
    # When I tried to do pytest it was unable to defined things like "fill"
    # So TA please comment out the method mentioned in the comment in order
    # for these methods to pass pytest. Thank you!


def test_player_update():
    # NEEDS TA ACTION!!! For this one please comment out
    # self.flip_tiles(x, y, True) from player_update in disks.py
    d = Disks(400, 400, 100, gr)
    d.player_update(50, 150)
    assert d.black_score == 2
    assert d.gr.player_turn is True
    gr1 = GameRef(gc, 100)
    d1 = Disks(400, 400, 100, gr1)
    d1.legal_table = set([(1, 0)])
    d1.player_update(50, 150)
    assert d1.black_score == 3
    assert d1.gr.player_turn is False
    gr2 = GameRef(gc, 100)
    d2 = Disks(400, 400, 100, gr2)
    d2.legal_table = set([(1, 0)])
    d2.table[1][0] = 3
    d2.player_update(50, 150)
    assert d2.black_score == 2
    assert d2.gr.player_turn is True
    gr3 = GameRef(gc, 100)
    d3 = Disks(400, 400, 100, gr3)
    d3.legal_table = set([(1, 2)])
    d3.player_update(250, 150)
    assert d3.black_score == 2
    assert d3.gr.player_turn is True


def test_computer_update():
    # NEEDS TA ACTION!!! For this one please comment out
    # elf.flip_tiles(x, y, True) from computer_update in disks.py
    gr4 = GameRef(gc, 100)
    d4 = Disks(400, 400, 100, gr4)
    d4.computer_update(50, 150)
    assert d4.white_score == 3
    assert d4.gr.player_turn is True


def test__flip_tiles_one_dir():
    # NEEDS TA ACTION!!! _flip_tiles_one_dir contains display,
    # please comment out everything below if next result:....
    gr5 = GameRef(gc, 100)
    d5 = Disks(400, 400, 100, gr5)
    assert d5._flip_tiles_one_dir((5, 0), d5._move_right, True) is False
    gr6 = GameRef(gc, 100)
    d6 = Disks(400, 400, 100, gr6)
    assert d6._flip_tiles_one_dir((1, 0), d6._move_right, True) is False
    gr7 = GameRef(gc, 100)
    d7 = Disks(400, 400, 100, gr7)
    assert d7._flip_tiles_one_dir((1, 2), d6._move_right, True) is True


def test_move_right():
    """Test if the method correctly return the coordinate on the right
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 0)
    assert d._move_right(position) == (0, 1)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -2)
    assert d._move_right(position) == (-1, -1)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_right(position) == (3, 8)


def test_move_left():
    """Test if the method correctly return the coordinate on the left
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_left(position) == (0, 0)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_left(position) == (-1, -4)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_left(position) == (3, 6)


def test_move_up():
    """Test if the method correctly return the coordinate on the above
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_up(position) == (-1, 1)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_up(position) == (-2, -3)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_up(position) == (2, 7)


def test_move_down():
    """Test if the method correctly return the coordinate on the down
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_down(position) == (1, 1)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_down(position) == (0, -3)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_down(position) == (4, 7)


def test_move_left_up():
    """Test if the method correctly return the coordinate on the upper left
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_left_up(position) == (-1, 0)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_left_up(position) == (-2, -4)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_left_up(position) == (2, 6)


def test_move_left_down():
    """Test if the method correctly return the coordinate on the left down
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_left_down(position) == (1, 0)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_left_down(position) == (0, -4)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_left_down(position) == (4, 6)


def test_move_right_up():
    """Test if the method correctly return the coordinate on the upper right
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_right_up(position) == (-1, 2)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_right_up(position) == (-2, -2)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_right_up(position) == (2, 8)


def test_move_right_down():
    """Test if the method correctly return the coordinate on the right down
    of current position."""
    d = Disks(100, 100, 50, gr)
    position = (0, 1)
    assert d._move_right_down(position) == (1, 2)
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d._move_right_down(position) == (0, -2)
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._move_right_down(position) == (4, 8)


def test_is_position_valid():
    """Test if the method correctly return the boolean of a given position
    that is within the board size.."""
    d = Disks(100, 100, 50, gr)
    position = (0, 0)
    assert d._is_position_valid(position) is True
    d1 = Disks(100, 100, 50, gr)
    position = (-1, -3)
    assert d1._is_position_valid(position) is False
    d2 = Disks(100, 100, 50, gr)
    position = (3, 7)
    assert d2._is_position_valid(position) is False


def test_check_adjacent():
    """Test if the method correctly check the adjacent position
    for legal moves."""
    d = Disks(400, 400, 100, gr)
    d.check_adjacent(1, 1, 0, -1, True)
    assert d.legal_table == set([(1, 0)])
    d1 = Disks(400, 400, 100, gr)
    d1.check_adjacent(1, 3, 0, 1, True)
    assert d1.legal_table == set([(1, 3)])
    d2 = Disks(400, 400, 100, gr)
    d2.check_adjacent(2, 1, 1, 0, False)
    assert d2.legal_table == set([(3, 1)])


def test_check_legal():
    """Test if the method store correct legal moves into the set."""
    d = Disks(400, 400, 100, gr)
    d.check_legal(True)
    assert d.legal_table == set([(1, 0), (0, 1), (2, 3), (3, 2)])
    d1 = Disks(800, 800, 100, gr)
    d1.check_legal(False)
    assert d1.legal_table == set([(2, 4), (3, 5), (4, 2), (5, 3)])
