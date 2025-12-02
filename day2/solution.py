from pathlib import Path

def parse_input(file):
    with open(file) as f:
        ranges = f.read().strip().split(",")
        return [tuple(map(int, r.split("-"))) for r in ranges]


def divisors_of(length):
    for i in range(2, length + 1):
        if length % i == 0:
            yield i


def sum_invalids(data, is_invalid):
    return sum(x for (a, b) in data for x in range(a, b+1) if is_invalid(str(x)))


def part1(data):
    inv = lambda s: s == s[:len(s)//2]*2
    return sum_invalids(data, inv)


def part2(data):
    inv = lambda s: any(s == s[:len(s)//k]*k for k in (divisors_of(len(s))))
    return sum_invalids(data, inv)


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")

if __name__ == "__main__":
    main()