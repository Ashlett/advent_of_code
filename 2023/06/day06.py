
if __name__ == '__main__':

    from day06_lib import get_ways_to_win_multiplied, get_ways_to_win_long_race

    with open("input_day6.txt", "r") as f:
        race_input = f.read()

    print("part 1:", get_ways_to_win_multiplied(race_input))
    print("part 2:", get_ways_to_win_long_race(race_input))
