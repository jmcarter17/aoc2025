from itertools import zip_longest, groupby
from pathlib import Path
from math import prod

from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        *lines, ops = [line.strip("\n") for line in f]
        ops = [(sum if op == "+" else prod) for op in ops.split()]
        return lines, ops


@timer
def part1(lines, ops):
    data = [[int(x) for x in line.split()] for line in lines]
    operands = zip(*data)
    return sum(op(col) for op, col in zip(ops, operands))


@timer
def part2(lines, ops):
    operands = [
        (int("".join(x)) if any(c != " " for c in x) else None)
        for x in zip_longest(*lines, fillvalue=" ")
    ]
    grouped = groupby(operands, lambda x: x is not None)
    columns = [list(g) for k, g in grouped if k]
    return sum(op(col) for op, col in zip(ops, columns))


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(*data)
    part2(*data)


if __name__ == "__main__":
    main()
