def part_1(input_text: str) -> int:
    return sum_extrapolated_values(input_text, extrapolate_forward)


def part_2(input_text: str) -> int:
    return sum_extrapolated_values(input_text, extrapolate_backward)


def sum_extrapolated_values(input_text: str, extrapolation_function) -> int:
    history = input_text.splitlines()
    values_sum = 0

    for line in history:
        numbers = [int(n) for n in line.split()]
        extrapolation = [numbers]
        while not all([n == 0 for n in numbers]):
            numbers = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
            extrapolation.append(numbers)

        values_sum += extrapolation_function(extrapolation)

    return values_sum


def extrapolate_forward(extrapolation) -> int:
    next_value = 0
    for ex in reversed(extrapolation):
        next_value = next_value + ex[-1]
    return next_value


def extrapolate_backward(extrapolation) -> int:
    prev_value = 0
    for ex in reversed(extrapolation):
        prev_value = ex[0] - prev_value
    return prev_value
