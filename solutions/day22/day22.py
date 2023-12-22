from functools import cache
import re

inp = [list(map(int, re.findall(r"\d+", line))) for line in open(0).readlines()]
inp.sort(key=lambda x: x[5])
N = len(inp)

bricks: list[list[tuple[int, int, int]]] = [
    [
        (x, y, z)
        for x in range(ax, bx + 1)
        for y in range(ay, by + 1)
        for z in range(az, bz + 1)
    ]
    for ax, ay, az, bx, by, bz in inp
]

parents = {i: set() for i in range(N + 1)}
floormap = [[(0, 0) for _ in range(10)] for _ in range(10)]  # highest point, brick id

# We will now drop down the bricks
for i, cubes in enumerate(bricks, 1):
    z_brick = min(z for _, _, z in cubes)
    z_floor = max(floormap[y][x][0] for x, y, _ in cubes)
    dz = z_brick - z_floor - 1

    for j, (x, y, z) in enumerate(cubes):
        cubes[j] = (x, y, z - dz)

        p, k = floormap[y][x]

        if p == z_floor:
            parents[k].add(i)

        floormap[y][x] = z - dz, i


@cache
def component_size(ignore):
    # Traverse the graph from floor ignoring a node, return the size of the component
    # Could be optimized.
    visited = set()
    stack = [0]
    while stack:
        i = stack.pop(0)
        if i in visited:
            continue
        visited.add(i)
        for j in parents[i]:
            if j != ignore + 1:
                stack.append(j)

    return len(visited)


def part1():
    return sum(component_size(i) == N for i in range(N))


def part2():
    return sum(N - component_size(i) for i in range(N))


print(part1(), part2())
