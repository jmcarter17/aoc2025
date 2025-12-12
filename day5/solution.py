from pathlib import Path
from functools import reduce

from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        ranges, ids = f.read().strip().split("\n\n")
    ranges = [tuple(map(int, line.strip().split("-"))) for line in ranges.splitlines()]
    ids = [int(line.strip()) for line in ids.splitlines()]
    return ranges, ids


@timer
def part1(ranges, ids):
    in_range = lambda id_: any(start <= id_ <= end for start, end in ranges)
    return sum(map(in_range, ids))


def merge_ranges(ranges):
    def merge_range(merged, current):
        start, end = current
        if not merged or merged[-1][1] < start - 1:
            return merged + [(start, end)]
        return merged[:-1] + [(merged[-1][0], max(merged[-1][1], end))]

    return reduce(merge_range, sorted(ranges), [])


@timer
def part2(ranges):
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(*data)
    part2(data[0])


if __name__ == "__main__":
    main()
