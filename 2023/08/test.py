import pytest

from lib import part_1, part_2

TEST_INPUT_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""


TEST_INPUT_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

TEST_INPUT_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (TEST_INPUT_1, 2),
        (TEST_INPUT_2, 6),
    )
)
def test_part_1(test_input, expected):
    assert part_1(test_input) == expected


def test_part_2():
    assert part_2(TEST_INPUT_3) == 6
