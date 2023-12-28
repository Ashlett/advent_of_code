
if __name__ == '__main__':

    from day03_lib import read_input, find_numbers, find_neighbors

    lines = read_input()
    gears = {}
    for number, line_number, start, end in find_numbers(lines):
        for x, y in find_neighbors(lines, line_number, start, end):
            if lines[x][y] == "*":
                gears.setdefault((x, y), []).append(int(number))

    result = 0
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            result += numbers[0] * numbers[1]
    print(result)
