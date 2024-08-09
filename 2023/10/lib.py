def part_1(input_text: str) -> int:
    matrix = input_text.splitlines()
    i, j = get_starting_point(matrix)
    # for neighbor in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
    #     new_i, new_j = neighbor
    #     if new_i > -1 and new_j > -1:
    #         point = matrix[new_i][new_j]
    #         if
    return 0


def get_starting_point(matrix):
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            point = line[j]
            if point == "S":
                return i, j


def part_2(input_text: str) -> int:
    return 0
