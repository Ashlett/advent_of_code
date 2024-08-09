import pytest
from lib import part_1, part_2, get_starting_point

SIMPLE_LOOP = """.....
.S-7.
.|.|.
.L-J.
.....
"""

SIMPLE_LOOP_WITH_EXTRA_PIPES = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

COMPLEX_LOOP = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

COMPLEX_LOOP_WITH_EXTRA_PIPES = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""


@pytest.mark.parametrize(
    "test_input, expected_num_steps",
    (
        (SIMPLE_LOOP, 4),
        (SIMPLE_LOOP_WITH_EXTRA_PIPES, 4),
        (COMPLEX_LOOP, 8),
        (COMPLEX_LOOP_WITH_EXTRA_PIPES, 8)
    )
)
def test_part_1(test_input, expected_num_steps):
    assert part_1(test_input) == expected_num_steps


def test_part_2():
    assert part_2(SIMPLE_LOOP) == 1


@pytest.mark.parametrize(
    "test_input, i, j",
    (
            (SIMPLE_LOOP, 1, 1),
            (SIMPLE_LOOP_WITH_EXTRA_PIPES, 1, 1),
            (COMPLEX_LOOP, 2, 0),
            (COMPLEX_LOOP_WITH_EXTRA_PIPES, 2, 0)
    )
)
def test_get_starting_point(test_input, i, j):
    assert get_starting_point(test_input.splitlines()) == (i, j)
