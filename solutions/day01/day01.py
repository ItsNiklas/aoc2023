inp: list[str] = open(0).readlines()


def part1():
    # sum = 0
    # for line in inp:
    #     ints = [int(c) for c in line if c.isnumeric()]
    #     sum += ints[0] * 10 + ints[-1]

    # return sum

    return sum(
        int(ints[0] + ints[-1]) for ints in (list(filter(str.isdigit, line)) for line in inp)
    )


def part2():
    global inp

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

    def process(line):
        for k, v in spell.items():
            line = line.replace(k, v)
        return line
    
    inp = map(lambda line: process(line), inp)
    return part1()


print(part1(), part2())
