from collections import Counter
from pathlib import Path

from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        start, *rows = [l.strip() for l in f if l.strip()]
        start = start.index("S")
        splitters = [{i for i, c in enumerate(row) if c == "^"} for row in rows if "^" in row]
        return start, splitters

@timer
def part1(start, splitters):
    beams = {start}
    count = 0
    for split_positions in splitters:
        hits = beams & split_positions
        count += len(hits)
        beams -= hits
        for hit in hits:
            beams |= {hit - 1, hit + 1}
    return count

@timer
def part2(start, splitters):
    beams = Counter()
    beams[start] = 1
    for row in splitters:
        new_beams = Counter()
        hits = beams.keys() & row
        misses = beams.keys() - hits
        for hit in hits:
            new_beams[hit - 1] += beams[hit]
            new_beams[hit + 1] += beams[hit]
        for miss in misses:
            new_beams[miss] += beams[miss]
        beams = new_beams
    return beams.total()


def main():
    folder = Path(__file__).resolve().parent
    start, splitters = parse_input(folder / "input.txt")
    print(f"part1: {part1(start, splitters)}")
    print(f"part2: {part2(start, splitters)}")


if __name__ == "__main__":
    main()
