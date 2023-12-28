
def read_input():
    with open("input_day3.txt", "r") as f:
        return f.read().splitlines(keepends=False)


def is_symbol(char):
    return not char == "." and not char.isdigit()


def find_numbers(matrix):
    for i, row in enumerate(matrix):
        j = 0
        number = ""
        while j < len(row):
            current = row[j]
            if current.isdigit():
                if not number:
                    number_start = j
                number += current
            else:
                if number:
                    yield number, i, number_start, j
                    number = ""
            j += 1
        if number:
            yield number, i, number_start, j


def find_neighbors(matrix, line_number, start, end):
    row = matrix[line_number]
    if start != 0:  # number doesn't start on 1st column
        yield line_number, start - 1
        check_start = start - 1
    else:
        check_start = start
    if end == len(row):  # number ends where line ends?
        check_end = end
    else:
        yield line_number, end
        check_end = end + 1
    if line_number != 0:  # not 1st line
        x = line_number - 1
        for y in range(check_start, check_end):
            yield x, y
    if line_number < len(matrix) - 1:  # not last line
        x = line_number + 1
        for y in range(check_start, check_end):
            yield x, y


def is_adjacent_to_symbol(matrix, line_number, start, end) -> bool:
    for x, y in find_neighbors(matrix, line_number, start, end):
        if is_symbol(matrix[x][y]):
            return True
    return False
