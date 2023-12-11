from itertools import combinations, starmap

inp = open(0).read().splitlines()


def part1and2(age):
    def dist(a, b):
        (y1, x1), (y2, x2) = a, b

        exp = sum(min(x1, x2) < i < max(x1, x2) for i in idx) + sum(
            min(y1, y2) < i < max(y1, y2) for i in idy
        )

        return (d := abs(x2 - x1) + abs(y2 - y1)) + exp, d + age * exp

    idy = [i for i, v in enumerate(inp) if not "#" in v]
    idx = [i for i, v in enumerate(zip(*inp)) if not "#" in v]

    galaxies = (
        (i, j) for j in range(len(inp[0])) for i in range(len(inp)) if inp[i][j] == "#"
    )
    return map(sum, zip(*starmap(dist, combinations(galaxies, 2))))


print(*part1and2(1000000 - 1))
