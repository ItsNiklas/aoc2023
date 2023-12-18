from itertools import pairwise, starmap

inp = [x.split() for x in open(0).read().splitlines()]


def part1and2(hex=False):
    y, x = 0, 0
    pnts = [(y, x)]
    b = 0

    for d, k, c in inp:
        b += (k := int(c[2:7], 16) if hex else int(k))
        d = c[7] if hex else d

        match d:
            case "R" | "0":
                x += k
            case "D" | "1":
                y += k
            case "L" | "2":
                x -= k
            case "U" | "3":
                y -= k

        pnts.append((y, x))

    # Shoelace + Pick
    A = abs(sum(starmap(lambda a, b: a[0] * b[1] - a[1] * b[0], pairwise(pnts)))) // 2

    return A + b // 2 + 1


print(part1and2(), part1and2(True))
