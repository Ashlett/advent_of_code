def calculate_total_scratchcards(cards):
    cards_with_repetitions = [[card, 1] for card in cards]
    for index, (card, repetitions) in enumerate(cards_with_repetitions):
        _, numbers = card.split(":")
        winning, have = ([int(x) for x in y.split()] for y in numbers.split("|"))
        points = 0
        for number in have:
            if number in winning:
                points += 1
        for rep in range(repetitions):
            for point in range(points):
                cards_with_repetitions[index + point + 1][1] += 1

    return sum([x[1] for x in cards_with_repetitions])
