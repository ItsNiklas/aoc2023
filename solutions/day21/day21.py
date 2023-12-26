inp = open(0).read().splitlines()
N, M = len(inp), len(inp[0])
pos = {(N // 2, M // 2)}
visited: dict[tuple[int, int], int] = {(N // 2, M // 2): 0}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def step(num):
    global pos
    new_pos = set()
    for y, x in pos:
        for i in range(4):
            yn = y + dy[i]
            xn = x + dx[i]
            if 0 <= yn < N and 0 <= xn < M:
                if inp[yn][xn] != "#":
                    new_pos.add((yn, xn))
                    if (yn, xn) not in visited:
                        visited[(yn, xn)] = num

    pos = new_pos


def part1():
    for num in range(6 if N < 12 else 64):
        step(num + 1)

    return len(pos)


def part2():
    for num in range(6 if N < 12 else 64, N):
        step(num + 1)

    n, r = divmod(26501365, N)

    even_c = sum(map(lambda v: not v % 2 and v > r, visited.values()))
    even_f = sum(map(lambda v: not v % 2, visited.values()))

    odd_c = sum(map(lambda v: v % 2 and v > r, visited.values()))
    odd_f = sum(map(lambda v: v % 2, visited.values()))

    return (n + 1) ** 2 * odd_f + n**2 * even_f - (n + 1) * odd_c + n * even_c


print(part1(), part2())
