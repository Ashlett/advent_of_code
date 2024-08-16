def part_1(input_text: str) -> int:
    return sum_shortest_paths_in_expanded_universe(input_text, 2)


def part_2(input_text: str) -> int:
    return sum_shortest_paths_in_expanded_universe(input_text, 1000000)


def sum_shortest_paths_in_expanded_universe(input_text: str, expansion_factor: int = 2):
    galaxies = extract_galaxies(input_text)
    expanded_universe = expand_universe(galaxies, expansion_factor)

    sum_shortest_paths = 0
    for i, gal1 in enumerate(expanded_universe):
        for gal2 in expanded_universe[i + 1:]:
            x1, y1 = gal1
            x2, y2 = gal2
            sum_shortest_paths += calculate_shortest_path(x1, y1, x2, y2)

    return sum_shortest_paths


def extract_galaxies(input_text):
    galaxies = []
    for y, line in enumerate(input_text.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))
    return galaxies


def expand_universe(galaxies: list[tuple[int, int]], expansion_factor: int = 2) -> list[tuple[int, int]]:
    x_with_galaxies = set(gal[0] for gal in galaxies)
    y_with_galaxies = set(gal[1] for gal in galaxies)

    empty_x = [x for x in range(max(x_with_galaxies)) if x not in x_with_galaxies]
    empty_y = [y for y in range(max(y_with_galaxies)) if y not in y_with_galaxies]

    expanded_universe = []
    for x, y in galaxies:
        num_empty_x_before = len([e for e in empty_x if e < x])
        num_empty_y_before = len([e for e in empty_y if e < y])
        new_x = num_empty_x_before * (expansion_factor - 1) + x
        new_y = num_empty_y_before * (expansion_factor - 1) + y
        expanded_universe.append((new_x, new_y))

    return expanded_universe


def calculate_shortest_path(x1: int, y1: int, x2: int, y2: int):
    return abs(x2 - x1) + abs(y2 - y1)
