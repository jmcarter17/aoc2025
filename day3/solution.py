from pathlib import Path


def parse_input(file):
    with open(file) as f:
        return list(tuple(map(int, l.strip())) for l in f)


def max_joltage(digits, n):
    l = len(digits)
    k = l - n

    stack = []
    for d in digits:
        while k > 0 and stack and stack[-1] < d:
            stack.pop()
            k -= 1
        stack.append(d)

    return int("".join(map(str, stack[:n])))


def max_joltage_old(row, n):
    digits = []
    i = 0
    l = len(row)
    while n > 0:
        digits.append(max(row[i : l - n + 1]))
        i += row[i : l - n + 1].index(digits[-1]) + 1
        n -= 1
    return int("".join(map(str, digits)))


def part1(data):
    return sum(max_joltage_old(row, 2) for row in data)


def part2(data):
    return sum(max_joltage_old(row, 12) for row in data)


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "test_input.txt")
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")


if __name__ == "__main__":
    main()
