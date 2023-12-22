import sys


inp = open(0).read().splitlines()
N, M = len(inp), len(inp[0])
pos = {
    (0, 0, y, x) for y, line in enumerate(inp) for x, c in enumerate(line) if c == "S"
}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def printgrid():
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            print("O" if (y, x) in pos else c, end="", file=sys.stderr)
        print("", file=sys.stderr)


def step(i=0):
    global pos
    new_pos = set()
    for gy, gx, y, x in pos:
        for i in range(4):
            yn = y + dy[i]
            xn = x + dx[i]
            if 0 <= yn < N and 0 <= xn < M:
                if inp[yn][xn] != "#":
                    new_pos.add((gy, gx, yn, xn))
            else:
                ...

    pos = new_pos


def part1():
    for _ in range(6 if N < 12 else 64):
        step()

    return len(pos)


def part2():
    ...


print(part1(), part2())
