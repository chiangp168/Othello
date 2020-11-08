import re
import os.path

from score_sheet import ScoreSheet


def test_constructor():
    score_file_name = "test_score.txt"
    s = ScoreSheet(score_file_name)
    assert s.filename == "test_score.txt"
    assert s.opened_file is None


def test_read_top_score():
    score_file_name = "test_score.txt"
    # This file is completely empty.
    s = ScoreSheet(score_file_name)
    assert s.read_top_score(score_file_name) is None


def test_read_top_score_1():
    score_file_name = "test_top_score.txt"
    # This file has two recorded scores.
    s = ScoreSheet(score_file_name)
    s.record_score(("ken", 15))
    s.record_score(("Ooooo 143 f3", 10))
    assert s.read_top_score(score_file_name) == int(15)


def test_record_score():
    score_file_name = "create_new_score_sheet.txt"
    # Since this file does not exits yet, once the function is
    # called it will create a txt file named "create_new_score_sheet.txt"
    s = ScoreSheet(score_file_name)
    s.record_score(("hawaii", 11))
    if os.path.isfile(score_file_name):
        with open(score_file_name, "r") as f:
            first_line = next(f, None)
    assert first_line == "hawaii 11\n"


def test_record_score_1():
    score_file_name = "test_top_score.txt"
    s = ScoreSheet(score_file_name)
    s.record_score(("hotdog", 1))
    s.record_score(("mad_cow", 20))
    s.record_score(("mama_goose", 20))
    if os.path.isfile(score_file_name):
        with open(score_file_name, "r") as f:
            all_lines = [next(f) for x in range(5)]
    assert all_lines == (["mama_goose 20\n", "mad_cow 20\n", "ken 15\n",
                         "Ooooo 143 f3 10\n", "hotdog 1\n"])
