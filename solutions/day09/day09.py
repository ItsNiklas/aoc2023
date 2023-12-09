from itertools import pairwise
from functools import partial

inp = [list(map(int, line.split())) for line in open(0).readlines()]


def predict(hist, past=False):
    if all(x == 0 for x in hist):
        return 0

    return hist[0 if past else -1] + (-1 if past else 1) * predict(
        [b - a for a, b in pairwise(hist)], past
    )


def part1():
    return sum(map(predict, inp))


def part2():
    return sum(map(partial(predict, past=True), inp))


print(part1(), part2())
