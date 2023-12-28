MAX = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


if __name__ == '__main__':

    result = 0
    with open("input_day2.txt", "r") as f:
        for line in f:
            possible = True
            game, rest = line.split(":")
            game_id = game.split(" ")[1].strip(":")

            subsets = rest.split(";")
            for subset in subsets:
                cubes = subset.split(",")
                for cube in cubes:
                    number, color = cube.strip().split(" ")
                    if int(number) > MAX[color]:
                        possible = False

            if possible:
                result += int(game_id)

    print(result)
