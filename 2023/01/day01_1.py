
if __name__ == '__main__':

    result = 0
    with open("input_day1.txt", "r") as f:
        for line in f:
            digits = [char for char in line if char.isdigit()]
            first = digits[0]
            last = digits[-1]
            result += int(f"{first}{last}")

    print(result)
