from pathlib import Path
import numpy as np
from scipy.signal import convolve2d

from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        return np.array(
            [[(1 if char == "@" else 0) for char in line.strip()] for line in f]
        )


def removable(data):
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    neighbors = convolve2d(data, kernel, mode="same", boundary="fill", fillvalue=0)
    return (data == 1) & (neighbors < 4)


@timer
def part1(data):
    return np.sum(removable(data))


@timer
def part2(data):
    count = 0
    while True:
        removable_cells = removable(data)
        if not np.any(removable_cells):
            break
        count += np.sum(removable_cells)
        data[removable_cells] = 0
    return count


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
