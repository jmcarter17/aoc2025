from collections import defaultdict
from pathlib import Path


def parse_input(file):
    with open(file) as f:
        return [l.strip() for l in f]


def part1(data):
    count = 0
    indices = {data[0].index("S")}
    for line in data[1:]:
        for i, c in enumerate(line):
            if c == "^" and i in indices:
                count += 1
                indices.discard(i)
                indices.add(i - 1)
                indices.add(i + 1)
    return count


def part2(data):
    count = 1
    indices = defaultdict(int)
    indices[data[0].index("S")] = 1
    for line in data[1:]:
        for i, c in enumerate(line):
            if c == "^" and indices[i]:
                cur = indices[i]
                count += cur
                indices.pop(i)
                indices[i - 1] += cur
                indices[i + 1] += cur
    return count


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")


if __name__ == "__main__":
    main()
