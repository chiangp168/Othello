from disk import Disk


def test_constructor():
    """Test constructor"""
    d = Disk(100, 150, 50)
    assert d.x == 100
    assert d.y == 150
    assert d.CELL == 50
    d.draw_black = False
    assert d.draw_black is False
    assert d.column == 2
    assert d.row == 3


def test_repr():
    """Test__repr__"""
    d = Disk(100, 150, 50)
    d.draw_black = True
    assert repr(d) == "Black"
    d1 = Disk(100, 150, 50)
    d1.draw_black = False
    assert repr(d1) == "White"
