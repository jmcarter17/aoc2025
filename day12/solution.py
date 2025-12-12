from pathlib import Path

from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        return list(f)

@timer
def part1(data): ...

@timer
def part2(data): ...


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
