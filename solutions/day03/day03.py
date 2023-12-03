from math import prod
import string
import re


inp: list[str] = open(0).readlines()
schematic = "".join(inp)
nums: list[tuple[int, int, int]] = list(
    map(lambda m: (int(m.group(0)), m.start(), m.end()), re.finditer(r"(\d+)", schematic))
)

ll = len(inp[0])
dx = [-1, +1, -ll + 1, -ll, -ll - 1, ll - 1, +ll, ll + 1]


def part1():
    symbols = [i for i, c in enumerate(schematic) if c in string.punctuation and c != "."]

    return sum(
        num
        for num, start, end in nums
        if any((x + d in symbols) for d in dx for x in range(start, end))
    )


def part2():
    gears = [i for i, c in enumerate(schematic) if c == "*"]

    sum = 0

    # Inefficent!
    for x in gears:
        matches = {num for num, start, end in nums if any(start <= x + d < end for d in dx)}

        if len(matches) == 2:
            sum += prod(matches)

    return sum


print(part1(), part2())
