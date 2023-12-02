from math import prod

inp: list[str] = open(0).readlines()


def part1():
    limits = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for i, line in enumerate(inp, 1):
        # bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
        for n, v in map(lambda x: x.split(), line.split(":")[1].replace(";", ",").split(", ")):
            if int(n) > limits[v]:
                break
        else:
            sum += i

    return sum


def part2():
    sum = 0
    for line in inp:
        limits = {"red": 0, "green": 0, "blue": 0}
        for n, v in map(lambda x: x.split(), line.split(":")[1].replace(";", ",").split(", ")):
            limits[v] = max(limits[v], int(n))

        sum += prod(limits.values())

    return sum


print(part1(), part2())
