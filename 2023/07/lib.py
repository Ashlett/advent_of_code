card_order = "AKQJT98765432"
hand_type_order = [
    (5,),             # five of a kind
    (4, 1),           # four of a kind
    (3, 2),           # full house
    (3, 1, 1),        # three of a kind
    (2, 2, 1),        # two pair
    (2, 1, 1, 1),     # one pair
    (1, 1, 1, 1, 1),  # high card
]


def sort_order(hand):
    counts = {card: hand.count(card) for card in hand}
    counts = tuple(reversed(sorted(list(counts.values()))))
    return (hand_type_order.index(counts), ) + tuple(card_order.index(card) for card in hand)


def part_1(input_text: str) -> int:
    hands_and_bids = [line.split() for line in input_text.splitlines(keepends=False)]
    hands_and_bids.sort(key=lambda x: sort_order(x[0]), reverse=True)

    total_winnings = 0
    for rank, hand_and_bid in enumerate(hands_and_bids, start=1):
        _, bid = hand_and_bid
        total_winnings += rank * int(bid)
    return total_winnings


def part_2(input_text: str) -> int:
    return 0
