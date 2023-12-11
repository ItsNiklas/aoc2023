from functools import reduce
from itertools import batched

inp: list[str] = open(0).read().split("\n\n")
seeds: list[int] = list(map(int, inp.pop(0).split(": ")[1].split()))
ranges: list[list[tuple[int, int, int]]] = [
    [tuple(map(int, line.split())) for line in segment.splitlines()[1:]]
    for segment in inp
]


def part1():
    def almanac_map(vals: list[int], r: list[tuple[int, int, int]]) -> list[int]:
        res = vals.copy()

        for dest, src, length in r:
            for i in range(len(vals)):
                if src <= vals[i] < src + length:
                    res[i] += dest - src

        return res

    return min(reduce(almanac_map, ranges, seeds))


def part2():
    def almanac_map2(
        vals: list[tuple[int, int]], r: list[tuple[int, int, int]]
    ) -> list[tuple[int, int]]:
        res = []

        # Dark arts: I modify the collection while iterating over that same collection.
        for v, l in vals:
            for dest, src, length in r:
                offset = dest - src
                src_end = src + length - 1
                v_end = v + l - 1

                # v+l fully within range
                if src <= v <= src_end and src <= v_end <= src_end:
                    res.append((v + offset, l))
                    break

                # v+l starting in range
                elif v < src and src <= v_end <= src_end:
                    vals.append((v, src - v))
                    res.append((src + offset, v_end - src + 1))
                    break

                # v+l ending in range
                elif src <= v <= src_end and src_end < v_end:
                    res.append((v + offset, src_end - v + 1))
                    vals.append((src_end + 1, v_end - src_end))
                    break

                # v+l over everything
                elif v <= src and src_end <= v_end:
                    vals.append((v, src - v))
                    res.append((src + offset, length))
                    vals.append((src_end + 1, v_end - src_end))
                    break

            else:
                # v+l not at all in range
                res.append((v, l))

        return res

    new_seeds = list(map(tuple, batched(seeds, 2)))
    return min(x[0] for x in reduce(almanac_map2, ranges, new_seeds))


print(part1(), part2())
