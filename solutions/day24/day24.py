from itertools import combinations, permutations
import re
import sys
import numpy as np

inp = open(0).read().splitlines()
hails = [list(map(int, re.findall(r"-?\d+", line))) for line in inp]


def part1():
    bbmin = 7 if len(hails) < 10 else 200000000000000
    bbmax = 27 if len(hails) < 10 else 400000000000000

    res = 0

    for (ax, ay, az, avx, avy, avz), (bx, by, bz, bvx, bvy, bvz) in combinations(
        hails, 2
    ):
        az, avz, bz, bvz = 0, 0, 0, 0

        # Now we need to solve
        A = np.array([[avx, -bvx], [avy, -bvy]])
        try:
            t, s = np.linalg.solve(A, [bx - ax, by - ay])
        except:
            continue

        if any([t < 0, s < 0]):
            continue  # in the past

        ix, iy, iz = ax + t * avx, ay + t * avy, az + t * avz
        res += bbmin <= ix <= bbmax and bbmin <= iy <= bbmax  # in the bounding box

    return res


def part2():
    ...


print(part1(), part2())
