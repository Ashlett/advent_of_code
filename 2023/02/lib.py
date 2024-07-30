MAX = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def part_1(input_text: str) -> int:
    result = 0
    for line in input_text.splitlines():
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

    return result


def part_2(input_text: str) -> int:
    result = 0
    for line in input_text.splitlines():
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

    return result
