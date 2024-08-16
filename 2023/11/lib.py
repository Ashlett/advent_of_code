def part_1(input_text: str) -> int:
    expanded_universe = expand_universe(input_text)

    galaxies = []
    for y, line in enumerate(expanded_universe.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))

    sum_shortest_paths = 0
    for i, gal1 in enumerate(galaxies):
        for gal2 in galaxies[i + 1:]:
            x1, y1 = gal1
            x2, y2 = gal2
            sum_shortest_paths += calculate_shortest_path(x1, y1, x2, y2)

    return sum_shortest_paths


def part_2(input_text: str) -> int:
    return 0


def expand_universe(input_text: str) -> str:
    expanded_rows = []

    for line in input_text.splitlines():
        if all([char == "." for char in line]):
            expanded_rows.append(line)
        expanded_rows.append(line)

    columns_to_expand = []
    for col_num in range(len(expanded_rows[0])):
        if all([line[col_num] == "." for line in expanded_rows]):
            columns_to_expand.append(col_num)

    expanded_rows_and_columns = []
    for line in expanded_rows:
        expanded_line = ""
        for i, char in enumerate(line):
            if i in columns_to_expand:
                expanded_line += "."
            expanded_line += char
        expanded_rows_and_columns.append(expanded_line)

    return "\n".join(expanded_rows_and_columns) + "\n"


def calculate_shortest_path(x1: int, y1: int, x2: int, y2: int):
    return abs(x2 - x1) + abs(y2 - y1)
