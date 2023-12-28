import pytest

from day03_lib import is_symbol, is_adjacent_to_symbol, find_numbers

TEST_MATRIX = [
    ".........232.633....",
    ".............*......",
    "..%......798.638...+",
    ".......*....35......",
    "......#863...324*...",
    "...=..707..157*334..",
    "..654....592.....*..",
    "92..............370*",
    "815*....921.........",
    ".874..497........278",
]


@pytest.mark.parametrize(
    "char, expected",
    (
            (".", False),
            ("0", False),
            ("1", False),
            ("*", True),
            ("&", True),
    )
)
def test_is_symbol(char, expected):
    assert is_symbol(char) == expected


@pytest.mark.parametrize(
    "line_number, start, end, expected",
    (
            (0, 9, 12, False),
            (0, 13, 16, True),
            (9, 17, 20, False),
    )
)
def test_is_adjacent_to_symbol(line_number, start, end, expected):
    assert is_adjacent_to_symbol(TEST_MATRIX, line_number=line_number, start=start, end=end) == expected


def test_find_numbers_first():
    numbers = find_numbers(TEST_MATRIX)
    first = next(numbers)
    assert first == ("232", 0, 9, 12)


def test_find_numbers_last():
    numbers = find_numbers(TEST_MATRIX)
    while True:
        try:
            last = next(numbers)
        except StopIteration:
            break
    assert last == ("278", 9, 17, 20)
