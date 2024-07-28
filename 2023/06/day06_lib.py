def get_ways_to_win_multiplied(test_input: str):
    time_line, distance_line = test_input.splitlines(keepends=False)
    times = [int(t) for t in time_line.split()[1:]]
    distances = [int(d) for d in distance_line.split()[1:]]
    num_ways_to_win_multiplied = 1

    for time, distance in zip(times, distances):
        num_ways_to_win = 0

        for button_press_time in range(1, time):
            speed = button_press_time
            remaining_time = time - button_press_time
            distance_traveled = speed * remaining_time
            if distance_traveled > distance:
                num_ways_to_win += 1

        num_ways_to_win_multiplied *= num_ways_to_win

    return num_ways_to_win_multiplied
