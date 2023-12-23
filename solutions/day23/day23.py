import queue

inp = open(0).read().splitlines()
N, M = len(inp), len(inp[0])

start, end = (0, 1), (N - 1, M - 2)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
slope = {"v": 0, ">": 1, "^": 2, "<": 3}


def part1():
    # Djisktra with negative weights
    q = queue.PriorityQueue()
    q.put((0, start, 0))
    dist = {start: 0}

    while not q.empty():
        d, (y, x), lastdir = q.get()

        if (y, x) == end:
            continue

        for i in range(4):
            if i == (lastdir + 2) % 4:  # Can't go back
                continue

            ny, nx = y + dy[i], x + dx[i]

            if inp[ny][nx] != "#" and slope.get(inp[ny][nx], i) == i:
                if dist.get((ny, nx), float("inf")) > d - 1:
                    dist[(ny, nx)] = d - 1
                    q.put((d - 1, (ny, nx), i))

    return -dist[end]


def part2():
    # Compress the graph such that only the intersections of the maze are nodes.
    # Check all points and look for intersections
    nodes = {start, end}
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if (
                inp[y][x] == "."
                and sum(inp[y + dy[i]][x + dx[i]] != "#" for i in range(4)) > 2
            ):
                nodes.add((y, x))

    # Now we build edges between the nodes.
    edges = {node: [] for node in nodes}
    for y, x in nodes - {end}:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if inp[ny][nx] != "#":  # We now walk in this direction until we hit a node
                cnt, lastdir = 1, i

                while (ny, nx) not in nodes:
                    for j in range(4):
                        if j == (lastdir + 2) % 4:
                            continue

                        nny, nnx = ny + dy[j], nx + dx[j]

                        if inp[nny][nnx] != "#":
                            ny, nx, lastdir = nny, nnx, j
                            cnt += 1
                            break

                edges[(y, x)].append(((ny, nx), cnt))

    # We now have a small graph. It is weighted and undirected. We are trying to find the longest path in this graph (NP-hard). PyPy is fast enough to solve this (8s).
    def dfs_longest(node, visited, curr_w):
        nonlocal max_weight
        visited.add(node)

        if node == end:
            max_weight = max(max_weight, curr_w)
            return

        for target, w in edges.get(node, []):
            if target not in visited:
                dfs_longest(target, visited.copy(), curr_w + w)

    max_weight = 0
    dfs_longest(start, set(), 0)
    return max_weight


print(part1(), part2())
