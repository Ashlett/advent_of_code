from day06_lib import get_ways_to_win_multiplied, get_ways_to_win_long_race

TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200
"""


def test_get_ways_to_win_multiplied():
    assert get_ways_to_win_multiplied(TEST_INPUT) == 288


def test_get_ways_to_win_long_race():
    assert get_ways_to_win_long_race(TEST_INPUT) == 71503
