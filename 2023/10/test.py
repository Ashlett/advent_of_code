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


@pytest.mark.parametrize(
    "test_input, expected_num_enclosed_tiles",
    (
        (SIMPLE_LOOP, 1),
        (SIMPLE_LOOP_WITH_EXTRA_PIPES, 1),
        ("""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""", 4),
        ("""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
""", 4),
        (""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""", 8),
        ("""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""", 10),
    )
)
def test_part_2(test_input, expected_num_enclosed_tiles):
    assert part_2(test_input) == expected_num_enclosed_tiles


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
