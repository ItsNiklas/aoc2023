inp: list[str] = open(0).readlines()


def part1():
    return sum(
        int(ints[0] + ints[-1]) for ints in (list(filter(str.isdigit, line)) for line in inp)
    )


def part2():
    global inp
    
    spell = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def process(line):
        for k, v in spell.items():
            line = line.replace(k, k + v + k)
        return line
    
    inp = map(lambda line: process(line), inp)
    return part1()


print(part1(), part2())
