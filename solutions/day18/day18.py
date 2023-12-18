from itertools import pairwise, starmap

inp = [x.split() for x in open(0).read().splitlines()]


def part1():
    y, x = 0, 0
    b = [(y, x)]
    v = 0

    for d, k, _ in inp:
        v += int(k)

        match d:
            case "U":
                y -= int(k)
            case "D":
                y += int(k)
            case "L":
                x -= int(k)
            case "R":
                x += int(k)

        b.append((y, x))

    # Shoelace + Pick
    A = abs(sum(starmap(lambda a, b: a[0] * b[1] - a[1] * b[0], pairwise(b)))) // 2

    return A + v // 2 + 1


print(part1())
