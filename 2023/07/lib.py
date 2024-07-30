hand_type_order = [
    (5,),             # five of a kind
    (4, 1),           # four of a kind
    (3, 2),           # full house
    (3, 1, 1),        # three of a kind
    (2, 2, 1),        # two pair
    (2, 1, 1, 1),     # one pair
    (1, 1, 1, 1, 1),  # high card
]


def get_hand_type_index(hand):
    counts = {card: hand.count(card) for card in hand}
    counts = tuple(reversed(sorted(counts.values())))
    return hand_type_order.index(counts)


def sort_order(hand):
    card_order = "AKQJT98765432"
    return (get_hand_type_index(hand), ) + tuple(card_order.index(card) for card in hand)


def sort_order_with_jokers(hand):
    card_order = "AKQT98765432J"
    hand_type_index = get_hand_type_index(hand)
    if "J" in hand:
        for new_card in card_order[:-1]:
            new_hand = hand.replace("J", new_card)
            new_hand_type_index = get_hand_type_index(new_hand)
            if new_hand_type_index < hand_type_index:
                hand_type_index = new_hand_type_index
    return (hand_type_index, ) + tuple(card_order.index(card) for card in hand)


def get_total_winnings(input_text: str, sort_order_function) -> int:
    hands_and_bids = [line.split() for line in input_text.splitlines(keepends=False)]
    hands_and_bids.sort(key=lambda x: sort_order_function(x[0]), reverse=True)

    total_winnings = 0
    for rank, hand_and_bid in enumerate(hands_and_bids, start=1):
        _, bid = hand_and_bid
        total_winnings += rank * int(bid)
    return total_winnings


def part_1(input_text: str) -> int:
    return get_total_winnings(input_text, sort_order)


def part_2(input_text: str) -> int:
    return get_total_winnings(input_text, sort_order_with_jokers)
