from itertools import count, cycle
from math import lcm
import re

inp = open(0).readlines()
instr = inp[0].strip()
nodemap = {x: (y, z) for x, y, z in (re.findall("\w+", line) for line in inp[2:])}


def part1(node):
    for i, d in zip(count(1), cycle(instr)):
        node: str = nodemap[node][0 if d == "L" else 1]
        if node.endswith("Z"):
            return i


def part2():
    # Find cycle lengths.
    return lcm(*(part1(node) for node in nodemap.keys() if node.endswith("A")))


print(part1("AAA"), part2())
