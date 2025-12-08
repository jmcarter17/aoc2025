import math
from itertools import combinations, islice, product
from pathlib import Path
from functools import reduce
from operator import mul


def parse_input(file):
    with open(file) as f:
        return [tuple(map(int, l.strip().split(","))) for l in f]


def find(parent, point):
    if parent[point] != point:
        parent[point] = find(parent, parent[point])  # Path compression
    return parent[point]


def union(parent, p1, p2):
    root1, root2 = find(parent, p1), find(parent, p2)
    if root1 != root2:
        parent[root2] = root1
        return True
    return False


def build_sorted_pairs(data):
    """Build and sort all pairs by distance."""
    return sorted(combinations(data, 2), key=lambda pair: math.dist(pair[0], pair[1]))


def part1(data, n):
    parent = {point: point for point in data}
    sorted_pairs = build_sorted_pairs(data)

    # Build circuits by connecting pairs
    for p1, p2 in sorted_pairs[:n]:
        union(parent, p1, p2)

    # Group points by their root
    circuits = {}
    for point in data:
        root = find(parent, point)
        circuits.setdefault(root, []).append(point)

    # Get sizes of three largest circuits
    top3_sizes = sorted((len(circuit) for circuit in circuits.values()), reverse=True)[
        :3
    ]
    return reduce(mul, top3_sizes, 1)


def part2(data):
    parent = {point: point for point in data}
    sorted_pairs = build_sorted_pairs(data)

    # Connect pairs until all points are in one circuit
    num_components = len(data)
    for p1, p2 in sorted_pairs:
        merged = union(parent, p1, p2)
        if merged:
            num_components -= 1
            if num_components == 1:
                return p1[0] * p2[0]
    return None


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    print(f"part1: {part1(data, n=1000)}")
    print(f"part2: {part2(data)}")


if __name__ == "__main__":
    main()
