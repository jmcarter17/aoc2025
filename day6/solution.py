from itertools import zip_longest, groupby
from pathlib import Path
from math import prod


def parse_input(file):
    with open(file) as f:
        *operands, ops = [line.strip("\n") for line in f if line.strip()]
        ops = [(sum if op == "+" else prod) for op in ops.split()]
        return operands, ops


def part1(operands, ops):
    data = [[int(x) for x in line.split()] for line in operands]
    columns = zip(*data)
    return sum(op(col) for op, col in zip(ops, columns))


def part2(operands, ops):
    operands = [
        (int("".join(x)) if any(c != " " for c in x) else None)
        for x in zip_longest(*operands, fillvalue=" ")
    ]
    grouped = groupby(operands, lambda x: x is not None)
    columns = [list(g) for k, g in grouped if k]
    return sum(op(col) for op, col in zip(ops, columns))


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    print(f"part1: {part1(*data)}")
    print(f"part2: {part2(*data)}")


if __name__ == "__main__":
    main()
