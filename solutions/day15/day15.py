inp = open(0).read().strip().split(",")


def HASH(s: str) -> int:
    v = 0

    for c in s:
        v += ord(c)
        v *= 17
        v %= 256

    return v


def part1():
    return sum(map(HASH, inp))


def part2():
    HASHMAP: dict[int, list[tuple[str, str]]] = {i: [] for i in range(256)}

    for opcode in inp:
        if "-" in opcode:
            label, _ = opcode.split("-")
            box = HASH(label)

            HASHMAP[box] = [(a, b) for a, b in HASHMAP[box] if a != label]

        if "=" in opcode:
            label, f = opcode.split("=")
            box = HASH(label)

            if label in map(lambda x: x[0], HASHMAP[box]):
                HASHMAP[box] = [(a, b if a != label else f) for a, b in HASHMAP[box]]
            else:
                HASHMAP[box].append((label, f))

    return sum(
        (box + 1) * i * int(f)
        for box, l in HASHMAP.items()
        for i, (_, f) in enumerate(l, 1)
    )


print(part1(), part2())
