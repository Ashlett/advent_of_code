DIGIT_STRINGS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_1(input_text: str) -> int:
    result = 0
    for line in input_text.splitlines():
        digits = [char for char in line if char.isdigit()]
        first = digits[0]
        last = digits[-1]
        result += int(f"{first}{last}")

    return result


def part_2(input_text: str) -> int:
    result = 0
    for line in input_text.splitlines():
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for string, digit in DIGIT_STRINGS.items():
                    if line[i:i + len(string)] == string:
                        digits.append(digit)

        first = digits[0]
        last = digits[-1]
        result += int(f"{first}{last}")

    return result
