inp: list[str] = open(0).readlines()
cards: list[tuple[list[int], list[int]]] = [
    tuple(list(map(int, part.strip().split())) for part in line.split(": ")[1].split(" | "))
    for line in inp
]
N: int = len(cards)


def part1():
    return sum(2 ** (wins - 1) for win, have in cards if (wins := sum(x in win for x in have)))


def part2():
    res = {x: 1 for x in range(N)}

    for i, (win, have) in enumerate(cards):
        wins = sum(x in win for x in have)

        for j in range(min(wins, N - i)):
            res[i + j + 1] += res[i]

    return sum(res.values())


print(part1(), part2())
