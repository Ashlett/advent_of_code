
if __name__ == '__main__':

    from day03_lib import read_input, find_numbers, is_adjacent_to_symbol

    lines = read_input()
    result = 0
    for number, line_number, start, end in find_numbers(lines):
        if is_adjacent_to_symbol(lines, line_number, start, end):
            result += int(number)
    print(result)
