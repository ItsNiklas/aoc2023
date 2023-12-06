from math import prod

inp = list(map(lambda x: x.split(":")[1].split(), open(0).readlines()))


def part1(time, distance):
    return prod(map(part2, zip(time, distance)))


def part2(x):
    t, d = x
    return sum(i * (t - i) > d for i in range(t + 1))


print(part1(*[map(int, l) for l in inp]), part2([int("".join(l)) for l in inp]))
