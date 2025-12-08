import math
from itertools import combinations, islice, product
from pathlib import Path
from functools import reduce
from operator import mul

def parse_input(file):
    with open(file) as f:
        return [tuple(map(int, l.strip().split(","))) for l in f]


def part1(data):
    all_pairs = combinations(data, 2)
    sorted_pairs = sorted(all_pairs, key=lambda pair: math.dist(pair[0], pair[1]))
    first_n = islice(sorted_pairs, 1000)
    circuits = []
    for p1, p2 in first_n:
        to_merge = []
        for i, circuit in enumerate(circuits):
            if p1 in circuit or p2 in circuit:
                circuit |= {p1, p2}
                to_merge.append(i)
        if to_merge:
            base = circuits[to_merge[0]]
            for i in reversed(to_merge[1:]):
                base |= circuits[i]
                del circuits[i]
        else:
            circuits.append({p1, p2})
    sorted_circuits = sorted(circuits, key=len, reverse=True)
    print(sorted_circuits)
    return reduce(mul, (len(circuit) for circuit in list(sorted_circuits)[:3]), 1)


def part2(data):
    full_len = len(data)
    all_pairs = combinations(data, 2)
    sorted_pairs = sorted(all_pairs, key=lambda pair: math.dist(pair[0], pair[1]))
    circuits = []
    for p1, p2 in sorted_pairs:
        to_merge = []
        for i, circuit in enumerate(circuits):
            if p1 in circuit or p2 in circuit:
                circuit |= {p1, p2}
                to_merge.append(i)
        if to_merge:
            base = circuits[to_merge[0]]
            for i in reversed(to_merge[1:]):
                base |= circuits[i]
                del circuits[i]
        else:
            circuits.append({p1, p2})
        if len(circuits) == 1 and len(circuits[0]) == full_len:
            return p1[0] * p2[0]


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    # print(data)
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")

if __name__ == "__main__":
    main()