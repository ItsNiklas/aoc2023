from itertools import count


dish = list(zip(*open(0).read().splitlines()))[::-1]


def tilt(line: tuple) -> list:
    line, k = list(line), len(line)

    for i in range(N := k):
        match line[i]:
            case "O":
                line[i] = "."
                line[N - k] = "O"
                k -= 1

            case "#":
                k = N - i - 1

    return line


def score(line: tuple) -> int:
    return sum(i for i, v in enumerate(line[::-1], 1) if v == "O")


def part1():
    return sum(map(score, map(tilt, dish)))


def part2():
    global dish
    states = []

    for i in count():
        for _ in range(4):  # Spin: Tilt and Rotate 4x
            dish = list(zip(*map(tilt, dish[::-1])))

        if dish in states:  # Cycle found, extrapolate
            x = states.index(dish)
            clen = i - x
            return sum(map(score, states[((1000000000 - x) % clen) + x - 1]))
        
        states.append(dish)


print(part1(), part2())
