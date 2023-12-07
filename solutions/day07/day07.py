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


def hand_power(hand: str) -> str:
    if cardmap["J"] != "11" and 0 < hand.count("J") < 5:
        # Replace Joker card with optimal card
        hand = hand.replace("J", Counter(hand.replace("J", "")).most_common(1).pop()[0])

    cnt = list(Counter(hand).values())

    match max(cnt):
        case 5:
            return "6"  # Five of a kind
        case 4:
            return "5"  # Four of a kind
        case 3:
            return "4" if cnt.count(2) == 1 else "3"  # Full House or Three of a kind
        case _:
            match cnt.count(2):
                case 2:
                    return "2"  # Two Pair
                case 1:
                    return "1"  # One Pair
                case _:
                    return ""  # High card


def hand_eval(hand: str) -> int:
    return int(hand_power(hand) + "".join(map(cardmap.get, hand)))


def part1():
    return sum(i * v[1] for i, v in enumerate(sorted(inp, key=lambda x: hand_eval(x[0])), 1))


def part2():
    cardmap["J"] = "01"

    return part1()


print(part1(), part2())
