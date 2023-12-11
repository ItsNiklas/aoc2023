from math import prod

inp: list[str] = open(0).readlines()


def part1():
    limits = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for i, line in enumerate(inp, 1):
        for n, v in line:
            if int(n) > limits[v]:
                break
        else:
            sum += i

    return sum


def part2():
    sum = 0
    for line in inp:
        limits = {"red": 0, "green": 0, "blue": 0}
        for n, v in line:
            limits[v] = max(limits[v], int(n))

        sum += prod(limits.values())

    return sum


inp = [
    list(map(lambda x: x.split(), line.split(":")[1].replace(";", ",").split(", ")))
    for line in inp
]
print(part1(), part2())
