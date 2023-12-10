from itertools import pairwise, starmap

inp = open(0).readlines()
N, M = len(inp), len(inp[0].strip())

pipes = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(0, 1), (1, 0), (0, -1), (-1, 0)],
    ".": [(0, 0)],
}


def loop() -> list[tuple[int, int]]:
    cy, cx = next((i, j) for j in range(M) for i in range(N) if inp[i][j] == "S")
    prev, main = (0, 0), []

    while True:
        d = [p for p in pipes[inp[cy][cx]] if p != prev]

        main.append((cy, cx))

        for dy, dx in d:
            ny, nx = cy + dy, cx + dx
            if inp[ny][nx] == "S":
                return main
            if (prev := (-dy, -dx)) in pipes[inp[ny][nx]]:
                cy, cx = ny, nx
                break


def part1() -> int:
    return len(loop()) // 2


def part2() -> int:
    l = loop()
    l.append(l[0])

    # Shoelace
    A = abs(sum(starmap(lambda a, b: a[0] * b[1] - a[1] * b[0], pairwise(l)))) // 2

    # Pick's Theorem
    return A - len(l) // 2 + 1


print(part1(), part2())
