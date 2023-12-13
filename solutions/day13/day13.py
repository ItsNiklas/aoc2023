def mirror(line: str, n: int) -> bool:
    # Check if n is a mirror line
    # Return amount of mismatches
    # n is column directly right of the mirror
    m = min(len(line[:n]), len(line[n:]))

    a = line[n - m : n]
    b = line[n : n + m][::-1]

    return sum(a[i] != b[i] for i in range(len(a)))


def part1and2():
    res1, res2 = 0, 0

    for block in inp:
        N, M = len(block[0]), len(block)
        mirror_counts = {
            col: sum(mirror(line, col) for line in block) for col in range(1, N)
        }
        res1 += sum(col for col, count in mirror_counts.items() if count == 0)
        res2 += sum(col for col, count in mirror_counts.items() if count == 1)

        # Horizontal line
        mirror_counts = {
            col: sum(mirror(line, col) for line in zip(*block)) for col in range(1, M)
        }
        res1 += 100 * sum(col for col, count in mirror_counts.items() if count == 0)
        res2 += 100 * sum(col for col, count in mirror_counts.items() if count == 1)

    return res1, res2


inp = list(block.splitlines() for block in open(0).read().split("\n\n"))


print(*part1and2())
