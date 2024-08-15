CONNECTORS = {
    "|": {"N", "S"},  # vertical pipe connecting north and south
    "-": {"E", "W"},  # horizontal pipe connecting east and west
    "L": {"N", "E"},  # 90-degree bend connecting north and east
    "J": {"N", "W"},  # 90-degree bend connecting north and west
    "7": {"S", "W"},  # 90-degree bend connecting south and west
    "F": {"S", "E"},  # 90-degree bend connecting south and east
}

DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}


OPPOSITES = {"N": "S", "S": "N", "E": "W", "W": "E"}


def part_1(input_text: str) -> int:
    matrix = input_text.splitlines()
    i, j = get_starting_point(matrix)

    paths = []

    for direction in DIRECTIONS:
        diff_i, diff_j = DIRECTIONS[direction]
        new_i, new_j = i + diff_i, j + diff_j
        from_direction = OPPOSITES[direction]
        connector = matrix[new_i][new_j]
        if connector in CONNECTORS:
            connector_directions = CONNECTORS[connector]
            if from_direction in connector_directions:
                next_direction = (connector_directions - {from_direction}).pop()
                path = [(new_i, new_j, next_direction)]
                paths.append(path)

    steps = 1

    while not paths[0][-1][:2] == paths[1][-1][:2]:
        for path in paths:
            i, j, direction = path[-1]
            diff_i, diff_j = DIRECTIONS[direction]
            new_i, new_j = i + diff_i, j + diff_j
            from_direction = OPPOSITES[direction]
            connector = matrix[new_i][new_j]
            connector_directions = CONNECTORS[connector]
            next_direction = (connector_directions - {from_direction}).pop()
            path.append((new_i, new_j, next_direction))
        steps += 1

    return steps


def get_starting_point(matrix):
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            point = line[j]
            if point == "S":
                return i, j


def part_2(input_text: str) -> int:
    return 0
