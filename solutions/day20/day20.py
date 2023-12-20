from itertools import count, takewhile
from dataclasses import dataclass, field
from math import prod


@dataclass
class Module:
    dests: list[str]
    type: str
    state: int = 0
    memory: dict[str, int] = field(default_factory=dict)


splits = [line.split(" -> ") for line in open(0).read().splitlines()]
modules: dict[str, Module] = {x[1:]: Module(y.split(", "), x[0]) for x, y in splits}

for k, module in modules.items():
    for dest in module.dests:
        if dest == "rx":
            rxchild = k
        elif modules[dest].type == "&":
            modules[dest].memory[k] = 0  # parse all input connections for '&' modules

lastsends = {k: [0, 0] for k in modules}
remmod = []
expectedlen = sum(rxchild in m.dests for m in modules.values())


def solve_congruence(pairs):  # CRT, import sympy.ntheory.modular.solve_congruence
    N = prod(m for _, m in pairs)
    return sum(r * (ni := N // m) * pow(ni, -1, m) for r, m in pairs) % N


def button(i=0):
    n_low, n_high = 1, 0

    # start with low pulse to broadcaster.
    q = [(dest, 0, "roadcaster") for dest in modules["roadcaster"].dests]

    while q:
        m, pulse, fr = q.pop(0)
        n_low, n_high = n_low + (not pulse), n_high + (pulse)

        if m == "rx":
            pass

        elif modules[m].type == "%" and not pulse:
            modules[m].state = not modules[m].state  # low, flip
            q.extend((dest, modules[m].state, m) for dest in modules[m].dests)

        elif modules[m].type == "&":
            modules[m].memory[fr] = pulse

            # if all inputs high it sends a low pulse, else high pulse
            for dest in modules[m].dests:
                q.append((dest, (s := not all(modules[m].memory.values())), m))

                if dest == rxchild and s:  # Sending high to rxchild! Find cycle.
                    if i - lastsends[m][-1] == lastsends[m][-1] - lastsends[m][-2]:
                        remmod.append((i, i - lastsends[m][-1]))
                    else:
                        lastsends[m].append(i)

    return n_low, n_high


def part1():
    res = [button() for _ in range(1000)]
    return sum(dl for dl, _ in res) * sum(dh for _, dh in res)


def part2():
    for k in takewhile(lambda _: len(remmod) != expectedlen, count(1000)):
        button(k)

    return solve_congruence(remmod) + 1


print(part1(), part2())
