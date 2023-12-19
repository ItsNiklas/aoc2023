from math import prod
import re


workflow, parts = open(0).read().split("\n\n")
workflow = {
    key: re.split(r",\s*", values)
    for key, values in re.findall(r"(\w+)\{([^}]+)\}", workflow)
}
parts = [list(map(int, re.findall(r"\d+", p))) for p in parts.splitlines()]


def work(x, m, a, s, wf="in") -> bool:
    if wf not in workflow:
        return wf == "A"

    for rule in workflow[wf]:
        try:
            cond, nwf = rule.split(":")
            if eval(cond):
                return work(x, m, a, s, nwf)
        except ValueError:
            return work(x, m, a, s, rule)


def work2(  # I wish this was shorter but I haven't found a good way to deal with the four variables
    x: list[tuple[int, int]],
    m: list[tuple[int, int]],
    a: list[tuple[int, int]],
    s: list[tuple[int, int]],
    wf="in",
) -> int:
    if wf not in workflow:
        if wf == "A":
            return prod(d - c + 1 for var in [x, m, a, s] for (c, d) in var)
        else:
            return 0

    ir = 0
    for rule in workflow[wf]:
        try:
            cond, nwf = rule.split(":")
            var, symb, num = cond[0], cond[1], int(cond[2:])

            # Split interval based on condition, forward true to nwf
            true_list, false_list = [], []
            for c, d in eval(var):
                deval = d > num if symb == ">" else d < num
                ceval = c > num if symb == ">" else c < num

                if deval and ceval:  # Accept all
                    true_list.append((c, d))
                if not (deval or ceval):  # Reject all
                    false_list.append((c, d))

                if deval ^ ceval:  # Accept Half
                    if symb == ">":
                        true_list.append((num + 1, d))
                        false_list.append((c, num))
                    else:
                        true_list.append((c, num - 1))
                        false_list.append((num, d))

            match var:
                case "x":
                    ir += work2(true_list, m, a, s, nwf)
                    x = false_list
                case "m":
                    ir += work2(x, true_list, a, s, nwf)
                    m = false_list
                case "a":
                    ir += work2(x, m, true_list, s, nwf)
                    a = false_list
                case "s":
                    ir += work2(x, m, a, true_list, nwf)
                    s = false_list

        except ValueError:
            return work2(x, m, a, s, rule) + ir


def part1():
    return sum(sum(tup) for tup in parts if work(*tup))


def part2():
    return work2(*(([(1, 4000)],) * 4))


print(part1(), part2())
