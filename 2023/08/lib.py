import itertools


def part_1(input_text: str) -> int:
    instructions = input_text.splitlines()

    right_left = instructions[0]
    right_left_cycle = itertools.cycle(right_left)

    nodes = {}
    for line in instructions[2:]:
        node = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[node] = ({"L": left, "R": right})

    current = "AAA"
    steps_count = 0

    while current != "ZZZ":
        turn = next(right_left_cycle)
        current = nodes[current][turn]
        steps_count += 1

    return steps_count


def part_2(input_text: str) -> int:
    instructions = input_text.splitlines()

    right_left = instructions[0]
    right_left_cycle = itertools.cycle(right_left)

    nodes = {}
    for line in instructions[2:]:
        node = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[node] = ({"L": left, "R": right})

    current = [n for n in nodes.keys() if n.endswith("A")]
    steps_count = 0

    while not all([n.endswith("Z") for n in current]):
        turn = next(right_left_cycle)
        current = [nodes[n][turn] for n in current]
        steps_count += 1

    return steps_count
