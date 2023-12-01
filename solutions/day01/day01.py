inp: list[str] = open(0).readlines()


def part1():
    sum = 0
    for line in inp:
        ints = [int(c) for c in line if c.isnumeric()]
        sum += ints[0] * 10 + ints[-1]

    return sum


def part2():
    spell = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    sum = 0
    for line in inp:
        for k, v in spell.items():
            line = line.replace(k, v)

        ints = [int(c) for c in line if c.isnumeric()]
        sum += ints[0] * 10 + ints[-1]

    return sum


print(part1(), part2())
