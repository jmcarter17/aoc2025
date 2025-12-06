from functools import reduce
from operator import add, mul
from pathlib import Path

def parse_input(file):
    with open(file) as f:
        data = [list(line) for line in f.read().split("\n") if line.strip()]
        max_len = max(len(line) for line in data)
        for row in data:
            row += [" "] * (max_len - len(row))
        return data

def compute(column):
    op = {
        '+': add,
        '*': mul,
    }
    return reduce(op[column[-1]], map(int, column[:-1]))

def part1(data):
    data = ["".join(line).rstrip() for line in data]
    columns = zip(*[line.split() for line in data])
    return sum(compute(col) for col in columns)


def extract_operations(ops_row):
    ops = []
    next_op = None
    count = 0
    for c in ops_row:
        if c in ('+', '*'):
            if next_op:
                ops.append((next_op, count))
            count = 0
            next_op = c
        else:
            count += 1
    ops.append((next_op, count+5))  # add some buffer to last count
    return ops

def part2(data):
    ops = extract_operations(data[-1])
    data = list("".join(x) for x in zip(*data[:-1]) if any(c != ' ' for c in x))
    i, count = 0, 0
    for op, l in ops:
        count += compute(data[i:i+l] + [op])
        i += l
    return count


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")

if __name__ == "__main__":
    main()