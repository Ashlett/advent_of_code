
if __name__ == '__main__':

    from day04_lib import calculate_total_scratchcards

    with open("input_day4.txt", "r") as f:
        cards = f.read().splitlines(keepends=False)

    print(calculate_total_scratchcards(cards))
