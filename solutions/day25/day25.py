from collections import defaultdict
from copy import deepcopy
import random


inp = open(0).read().splitlines()
connections = {x: y.split(" ") for x, y in (line.split(": ") for line in inp)}


def min_cut(graph, component_nodes):  # Min cut with Karger's algorithm
    def contract(u, v):
        component_nodes[u].update(component_nodes[v])  # Merge
        del component_nodes[v]

        for node in graph[v]:  # Update the graph
            if node != u:
                graph[u].append(node)
                graph[node].append(u)
            graph[node].remove(v)
        del graph[v]

    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        contract(u, v)

    a, b = component_nodes.values()

    if len(graph) == 2 and all(len(component) == 3 for component in graph.values()):
        return len(a), len(b)

    return False


def part1():
    graph = defaultdict(list)

    for node, l in connections.items():
        for n in l:
            graph[node].append(n)
            graph[n].append(node)

    while True:
        components = {node: {node} for node in graph}
        if sizes := min_cut(deepcopy(graph), components):
            return sizes[0] * sizes[1]


print(part1())
