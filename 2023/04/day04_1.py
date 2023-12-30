
if __name__ == '__main__':

    result = 0
    with open("input_day4.txt", "r") as f:
        for line in f:
            points = 0
            card, numbers = line.split(":")
            winning, have = ([int(x) for x in y.split()] for y in numbers.split("|"))
            for number in have:
                if number in winning:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            result += points

    print(result)
