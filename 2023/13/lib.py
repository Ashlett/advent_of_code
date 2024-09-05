def part_1(input_text: str) -> int:
    patterns = input_text.split("\n\n")
    result = 0
    for pattern in patterns:
        rows = pattern.splitlines()
        columns = transpose(rows)
        if mirror_line := find_mirror_line(columns):
            result += mirror_line
        if mirror_line := find_mirror_line(rows):
            result += mirror_line * 100

    return result


def find_mirror_line(lines) -> int | None:
    for possible in range(1, len(lines)):
        is_mirrored = False
        first = possible - 1
        second = possible
        if lines[first] == lines[second]:
            while first > 0 and second < len(lines) - 1:
                first -= 1
                second += 1
                if lines[first] != lines[second]:
                    break
            else:
                is_mirrored = True
        if is_mirrored:
            return possible


def transpose(rows):
    len_row = len(rows[0])
    columns = []
    for i in range(len_row):
        column = "".join(row[i] for row in rows)
        columns.append(column)
    return columns


def part_2(input_text: str) -> int:
    patterns = input_text.split("\n\n")
    result = 0
    for pattern in patterns:
        rows = pattern.splitlines()
        for new_rows in get_new_rows(rows):
            columns = transpose(new_rows)
            if mirror_line := find_mirror_line(columns):
                result += mirror_line
                break
            if mirror_line := find_mirror_line(new_rows):
                result += mirror_line * 100
                break

    return result


def get_new_rows(rows):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            new_rows = []
            old_char = rows[i][j]
            new_char = "#" if old_char == "." else "."
            for r, row in enumerate(rows):
                if r == i:
                    new_row = row[:j] + new_char + row[j + 1:]
                    new_rows.append(new_row)
                else:
                    new_rows.append(row)
            yield new_rows
