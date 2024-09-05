from lib import part_1, part_2

TEST_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


def test_part_1():
    assert part_1(TEST_INPUT) == 405


def test_part_2():
    assert part_2(TEST_INPUT) == 400
