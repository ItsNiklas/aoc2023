from itertools import combinations
import re
import numpy as np

inp = open(0).read().splitlines()
hails = [list(map(int, re.findall(r"-?\d+", line))) for line in inp]


def part1():
    bbmin = 7 if len(hails) < 10 else 200000000000000
    bbmax = 27 if len(hails) < 10 else 400000000000000

    res = 0

    for (ax, ay, _, avx, avy, _), (bx, by, _, bvx, bvy, _) in combinations(hails, 2):
        if (det := avx * (-bvy) - (-bvx) * avy) == 0:
            continue

        t = 1 / det * ((-bvy) * (bx - ax) - (-bvx) * (by - ay))
        s = 1 / det * (avx * (by - ay) - avy * (bx - ax))

        if any([t < 0, s < 0]):
            continue  # in the past

        ix, iy = ax + t * avx, ay + t * avy
        res += bbmin <= ix <= bbmax and bbmin <= iy <= bbmax  # in the bounding box

    return res


def part2():
    """
    9 unkowns: rx, ry, rz, rvx, rvy, rvz, t1, t2, t3
    9 equations:
    (rx - ax) / (avx - rvx) = t1
    (ry - ay) / (avy - rvy) = t1
    (rz - az) / (avz - rvz) = t1

    Combine x & y --> (rx - ax) + (avy - rvy) = (ry - ay) * (avx - rvx)
    rx * avy - rx * rvy - ax * avy + ax * rvy = ry * avx - ry * rvx - ay * avx + ay * rvx
    ry * rvx - rx * rvy = - rx * avy + ry * avx + ax * avy - ax * rvy - ay * avx + ay * rvx


    ry * rvx - rx * rvy = ay * rvx - ax * rvy + ry * avx - ay * avx - rx * avy + ax * avy
    ry * rvx - rx * rvy = by * rvx - bx * rvy + ry * bvx - by * bvx - rx * bvy + bx * bvy
    ry * rvx - rx * rvy = cy * rvx - cx * rvy + ry * cvx - cy * cvx - rx * cvy + cx * cvy

    Same for the other pairs
    rz * rvx - rx * rvz = az * rvx - ax * rvz + rz * avx - az * avx - rx * avz + ax * avz
    rz * rvx - rx * rvz = bz * rvx - bx * rvz + rz * bvx - bz * bvx - rx * bvz + bx * bvz
    rz * rvx - rx * rvz = cz * rvx - cx * rvz + rz * cvx - cz * cvx - rx * cvz + cx * cvz

    rz * rvy - ry * rvz = az * rvy - ay * rvz + rz * avy - az * avy - ry * avz + ay * avz
    rz * rvy - ry * rvz = bz * rvy - by * rvz + rz * bvy - bz * bvy - ry * bvz + by * bvz
    rz * rvy - ry * rvz = cz * rvy - cy * rvz + rz * cvy - cz * cvy - ry * cvz + cy * cvz


    And pair again
    (ay - by) * rvx - (ax + bx) * rvy + (avx - bvx) * ry - (avy + bvy) * rx = ay * avx - ax * avy - by * bvx + bx * bvy
    (ay - cy) * rvx - (ax + cx) * rvy + (avx - cvx) * ry - (avy + cvy) * rx = ay * avx - ax * avy - cy * cvx + cx * cvy

    (az - bz) * rvx - (ax + bx) * rvz + (avx - bvx) * rz - (avz + bvz) * rx = az * avx - ax * avz - bz * bvx + bx * bvz
    (az - cz) * rvx - (ax + cx) * rvz + (avx - cvx) * rz - (avz + cvz) * rx = az * avx - ax * avz - cz * cvx + cx * cvz

    (az - bz) * rvy - (ay + by) * rvz + (avy - bvy) * rz - (avz + bvz) * ry = az * avy - ay * avz - bz * bvy + by * bvz
    (az - cz) * rvy - (ay + cy) * rvz + (avy - cvy) * rz - (avz + cvz) * ry = az * avy - ay * avz - cz * cvy + cy * cvz

    And these are 6 linear equations in 6 unknowns, which we can solve.
    """

    ax, ay, az, avx, avy, avz = hails[0]
    bx, by, bz, bvx, bvy, bvz = hails[1]
    cx, cy, cz, cvx, cvy, cvz = hails[2]

    # Solving matrix for rx, ry, rz, rvx, rvy, rvz
    mat = np.array(
        [
            [avy - bvy, bvx - avx, 0, by - ay, ax - bx, 0],
            [avy - cvy, cvx - avx, 0, cy - ay, ax - cx, 0],
            [bvz - avz, 0, avx - bvx, az - bz, 0, bx - ax],
            [cvz - avz, 0, avx - cvx, az - cz, 0, cx - ax],
            [0, avz - bvz, bvy - avy, 0, bz - az, ay - by],
            [0, avz - cvz, cvy - avy, 0, cz - az, ay - cy],
        ]
    )

    b = np.array(
        [
            [by * bvx - bx * bvy - ay * avx + ax * avy],
            [cy * cvx - cx * cvy - ay * avx + ax * avy],
            [bx * bvz - bz * bvx - ax * avz + az * avx],
            [cx * cvz - cz * cvx - ax * avz + az * avx],
            [bz * bvy - by * bvz - az * avy + ay * avz],
            [cz * cvy - cy * cvz - az * avy + ay * avz],
        ]
    )

    rx, ry, rz, _, _, _ = map(int, np.around(np.linalg.solve(mat, b)))
    return rx + ry + rz


print(part1(), part2())
