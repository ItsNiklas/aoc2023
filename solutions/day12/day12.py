from functools import cache

inp = [line.split() for line in open(0).read().splitlines()]
inp = [(pat, tuple(map(int, cnts.split(",")))) for pat, cnts in inp]


@cache
def arrange(pat: str, cnts: tuple[int]) -> int:
    if not cnts:  # Empty blocks, no more '#'?
        return "#" not in pat

    if len(pat) < sum(cnts) + len(cnts):  # pat not long enough anymore?
        return 0

    match pat[0]:
        case ".":
            return arrange(pat[1:], cnts)

        case "?":  # Try both
            return arrange(pat[1:], cnts) + arrange("#" + pat[1:], cnts)

        case "#":  # We can match the next block and delimiter exists?
            bl = cnts[0]
            if "." not in pat[:bl] and pat[bl] != "#":
                return arrange(pat[bl + 1 :], cnts[1:])  # Cut off block + delimiter
    return 0


def part1():
    return sum(arrange(pat + ".", cnts) for pat, cnts in inp)


def part2():
    return sum(arrange("?".join([pat] * 5) + ".", cnts * 5) for pat, cnts in inp)


print(part1(), part2())
