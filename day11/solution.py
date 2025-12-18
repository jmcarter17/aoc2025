from functools import cache
from pathlib import Path
from utilities.timer import timer


def parse_input(file):
    graph = {}
    with open(file) as f:
        for l in f:
            nodes, edges = l.strip().split(":")
            graph[nodes] = edges.split()

    return graph


def count_simple_paths(graph, start, end):
    @cache
    def dfs(u):
        if u == end:
            return 1
        return sum(dfs(v) for v in graph.get(u, []))

    return dfs(start)


def count_simple_paths_filters(graph, start, end):
    @cache
    def dfs(u, seen_fft, seen_dac):
        if u == end and seen_fft and seen_dac:
            return 1
        return sum(dfs(v, seen_fft | v == "fft", seen_dac | v == "dac") for v in graph.get(u, []))

    return dfs(start, False, False)

@timer
def part1(graph):
    return count_simple_paths(graph, "you", "out")

@timer
def part2(graph):
    return (
        count_simple_paths(graph, "svr", "fft")
        * count_simple_paths(graph, "fft", "dac")
        * count_simple_paths(graph, "dac", "out")
    )


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
