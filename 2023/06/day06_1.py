
if __name__ == '__main__':

    from day06_lib import get_ways_to_win_multiplied

    with open("input_day6.txt", "r") as f:
        race_input = f.read()

    print(get_ways_to_win_multiplied(race_input))
