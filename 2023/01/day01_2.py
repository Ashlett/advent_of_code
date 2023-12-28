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


if __name__ == '__main__':

    result = 0
    with open("input_day1.txt", "r") as f:
        for line in f:
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

    print(result)
