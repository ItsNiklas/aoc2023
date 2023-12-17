from heapq import *

inp = open(0).read().splitlines()
N, M = len(inp), len(inp[0])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra(ultra=False):
    d, q = {}, []
    heappush(q, (0, 0, 0, -1, -1))

    while q:
        dist, y, x, dir, steps = heappop(q)

        if (y, x, dir, steps) in d:
            continue

        d[(y, x, dir, steps)] = dist
        
        for i in range(4):
            vy, vx = y + dy[i], x + dx[i]

            if not (0 <= vy < N) or not (0 <= vx < M):
                continue  # Out of bounds

            if ultra and i != dir and steps < 4 and dir != -1:
                continue  # Can I turn?

            if dir == (i + 2) % 4:
                continue  # No backsies

            if (new_steps := 1 if i != dir else steps + 1) > (10 if ultra else 3):
                continue  # Not again

            heappush(q, (dist + int(inp[vy][vx]), vy, vx, i, new_steps))

    return min(
        v
        for (y, x, _, steps), v in d.items()
        if y == N - 1 and x == M - 1 and (not ultra or steps >= 4)
    )


def part1():
    return dijkstra()


def part2():
    return dijkstra(True)


print(part1(), part2())
