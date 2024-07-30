def get_ways_to_win_one_race(time: int, distance: int) -> int:
    num_ways_to_win = 0

    for button_press_time in range(1, time):
        speed = button_press_time
        remaining_time = time - button_press_time
        distance_traveled = speed * remaining_time
        if distance_traveled > distance:
            num_ways_to_win += 1

    return num_ways_to_win


def part_1(input_text: str) -> int:
    time_line, distance_line = input_text.splitlines()
    times = [int(t) for t in time_line.split()[1:]]
    distances = [int(d) for d in distance_line.split()[1:]]
    num_ways_to_win_multiplied = 1

    for time, distance in zip(times, distances):
        num_ways_to_win_multiplied *= get_ways_to_win_one_race(time, distance)

    return num_ways_to_win_multiplied


def part_2(input_text: str) -> int:
    time_line, distance_line = input_text.splitlines()
    time = int("".join([t for t in time_line.split()[1:]]))
    distance = int("".join([t for t in distance_line.split()[1:]]))
    return get_ways_to_win_one_race(time, distance)
