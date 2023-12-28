
if __name__ == '__main__':

    result = 0
    with open("input_day2.txt", "r") as f:
        for line in f:
            fewest = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            game, rest = line.split(":")

            subsets = rest.split(";")
            for subset in subsets:
                cubes = subset.split(",")
                for cube in cubes:
                    number, color = cube.strip().split(" ")
                    count = int(number)
                    if count > fewest[color]:
                        fewest[color] = count

            power = fewest["red"] * fewest["green"] * fewest["blue"]
            result += power

    print(result)
