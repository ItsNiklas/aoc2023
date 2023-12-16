inp = open(0).read().splitlines()
N, M = len(inp), len(inp[0])


def beam(y, x, dy, dx) -> None:
    while True:
        if not (0 <= y < N) or not (0 <= x < M):
            return  # Out of bounds

        if (y, x, dy, dx) in visited:
            return  # Visited
        else:
            visited.add((y, x, dy, dx))

        match inp[y][x]:
            case "|":
                if dy == 0:  # Split
                    return beam(y - 1, x, -1, 0) or beam(y + 1, x, 1, 0)
            case "-":
                if dx == 0:  # Split
                    return beam(y, x - 1, 0, -1) or beam(y, x + 1, 0, 1)
            case "/":
                if dy == 0:
                    dy, dx = -dx, 0
                else:
                    dx, dy = -dy, 0
            case "\\":
                if dy == 0:
                    dy, dx = dx, 0
                else:
                    dx, dy = dy, 0

        y += dy
        x += dx


def part1(*start):
    global visited

    visited = set()
    beam(*start)
    return len(set((y, x) for y, x, _, _ in visited))


def part2():
    resY = max(max(part1(i, 0, 0, 1), part1(i, M - 1, 0, -1)) for i in range(N))
    resX = max(max(part1(0, j, 1, 0), part1(N - 1, j, -1, 0)) for j in range(M))

    return max(resY, resX)


print(part1(0, 0, 0, 1), part2())
