from math import prod
from pathlib import Path
from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        lines = [l.strip() for l in f]
        graph = {}
        for l in lines:
            nodes, edges = l.split(":")
            graph[nodes] = edges.split( ) if edges else []
        return graph


def count_simple_paths(graph, start, end):
    counts = {}
    def dfs(u):
        if u == end:
            return 1
        if u in counts:
            return counts[u]
        counts[u] = sum(dfs(v) for v in graph.get(u, []))
        return counts[u]

    return dfs(start)

@timer
def part1(graph):
    return count_simple_paths(graph, "you", "out")

@timer
def part2(graph):
    return prod((
        count_simple_paths(graph, "svr", "fft"),
        count_simple_paths(graph, "fft", "dac"),
        count_simple_paths(graph, "dac", "out"),
    )) + prod((
        count_simple_paths(graph, "svr", "dac"),
        count_simple_paths(graph, "dac", "fft"),
        count_simple_paths(graph, "fft", "out")
    ))


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
