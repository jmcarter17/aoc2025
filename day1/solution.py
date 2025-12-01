from itertools import accumulate, pairwise
from pathlib import Path

def parse_input(file):
    to_int = lambda x: (-1 if x[0] == 'L' else 1) * int(x[1:])
    with open(file) as f:
        return [to_int(x) for x in f]


def part1(data):
    return sum(x % 100 == 0 for x in accumulate(data, initial=50))


def part2(data):
    return sum(
        abs((y // 100) - (x // 100))
        + (1 if y % 100 == 0 and x > y else 0)
        - (1 if x % 100 == 0 and x > y else 0)
        for x, y in pairwise(accumulate(data, initial=50))
    )


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")

if __name__ == "__main__":
    main()