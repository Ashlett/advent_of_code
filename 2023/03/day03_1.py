
def read_input():
    with open("input_day3.txt", "r") as f:
        return f.read().splitlines(keepends=False)


def is_symbol(char):
    return not char == "." and not char.isdigit()


def is_adjacent_to_symbol(matrix, line_number, start, end) -> bool:
    row = matrix[line_number]
    if start != 0:  # number doesn't start on 1st column
        if is_symbol(row[start - 1]):
            return True
        check_start = start - 1
    else:
        check_start = start
    if end == len(row):  # number ends where line ends?
        check_end = end
    else:
        if is_symbol(row[end]):
            return True
        check_end = end + 1
    if line_number != 0:  # not 1st line
        for neighbor in matrix[line_number - 1][check_start:check_end]:
            if is_symbol(neighbor):
                return True
    if line_number < len(matrix) - 1:  # not last line
        for neighbor in matrix[line_number + 1][check_start:check_end]:
            if is_symbol(neighbor):
                return True

    return False


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
    result = 0
    for number, line_number, start, end in find_numbers(lines):
        if is_adjacent_to_symbol(lines, line_number, start, end):
            result += int(number)
    print(result)
