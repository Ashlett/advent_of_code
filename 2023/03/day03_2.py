

def read_input():
    with open("input_day3.txt", "r") as f:
        return f.read().splitlines(keepends=False)


def get_adjacent_gears(matrix, line_number, start, end) -> list[(int, int)]:
    coordinates = []
    row = matrix[line_number]
    if start != 0:  # number doesn't start on 1st column
        if row[start - 1] == "*":
            coordinates.append((line_number, start - 1))
        check_start = start - 1
    else:
        check_start = start
    if end == len(row):  # number ends where line ends?
        check_end = end
    else:
        if row[end] == "*":
            coordinates.append((line_number, end))
        check_end = end + 1
    if line_number != 0:  # not 1st line
        x = line_number - 1
        for y in range(check_start, check_end):
            if matrix[x][y] == "*":
                coordinates.append((x, y))
    if line_number < len(matrix) - 1:  # not last line
        x = line_number + 1
        for y in range(check_start, check_end):
            if matrix[x][y] == "*":
                coordinates.append((x, y))

    return coordinates


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


if __name__ == '__main__':

    lines = read_input()
    gears = {}
    result = 0
    for number, line_number, start, end in find_numbers(lines):
        for gear in get_adjacent_gears(lines, line_number, start, end):
            gears.setdefault(gear, []).append(int(number))
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            result += numbers[0] * numbers[1]
    print(result)
