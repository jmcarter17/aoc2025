from functools import reduce
from itertools import combinations
from pathlib import Path
from operator import xor

from utilities.timer import timer


def parse_line(l):
    mac, *switches, joltages = l.strip().split()
    macdigits = sum((1 if c == "#" else 0) << i for i, c in enumerate(mac[1:-1:--1]))
    switches_bin = [sum((1 << int(c)) for c in sw[1:-1].split(",")) for sw in switches]
    joltages = [int(j) for j in joltages[1:-1].split(",")]
    # print(bin(macdigits), [bin(s) for s in switches_bin], joltages)
    return macdigits, switches_bin, joltages


def parse_input(file):
    with open(file) as f:
        return list(zip(*[parse_line(l) for l in f.readlines()]))


def all_combinations(switches):
    for r in range(1, len(switches) + 1):
        for comb in combinations(switches, r):
            yield comb

@timer
def part1(machines, switches):
    lengths = []
    for mac, sw in zip(machines, switches):
        for sw_comb in all_combinations(sw):
            combined = reduce(xor, sw_comb, 0)
            if mac == combined:
                lengths.append(len(sw_comb))
                break
    return sum(lengths)


@timer
def part2(switches, jolts):
    print(switches[0], jolts[0])
    print(jolts)
    jolts = [sum(j << i for i, j in enumerate(jolt)) for jolt in jolts]
    print(jolts, [bin(j) for j in jolts])
    ...


def main():
    folder = Path(__file__).resolve().parent
    machines, switches, jolts = parse_input(folder / "input.txt")
    part1(machines, switches)
    part2(switches, jolts)


if __name__ == "__main__":
    main()
