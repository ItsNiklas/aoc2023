from collections import Counter

inp = [(line.split(" ")[0], int(line.split(" ")[1])) for line in open(0).readlines()]

cardmap = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}


def hand_power(card: str) -> str:
    if cardmap["J"] != "11" and 0 < card.count("J") < 5:
        # Replace Joker card with optimal card
        card = card.replace("J", Counter(card.replace("J", "")).most_common(1).pop()[0])

    cnt = list(Counter(card).values())

    if max(cnt) == 5:  # Five of a kind
        return "6"

    if max(cnt) == 4:  # Four of a kind
        return "5"

    if set(cnt) == {3, 2}:  # Full House
        return "4"

    if max(cnt) == 3:  # Three of a Kind
        return "3"

    if cnt.count(2) == 2:  # Two Pair
        return "2"

    if cnt.count(2) == 1:  # One Pair
        return "1"

    return ""  # High card


def hand(card: str) -> int:
    return int(hand_power(card) + "".join(map(cardmap.get, card)))


def part1():
    return sum(i * v[1] for i, v in enumerate(sorted(inp, key=lambda x: hand(x[0])), 1))


def part2():
    cardmap["J"] = "01"

    return part1()


print(part1(), part2())
