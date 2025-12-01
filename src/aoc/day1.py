from itertools import accumulate, pairwise

def get_data(file):
    to_int = lambda x: (-1 if x[0] == 'L' else 1) * int(x[1:])
    with open(file) as f:
        return [to_int(x) for x in f]


def part1(data):
    return sum(1 for x in accumulate([50] + data) if x % 100 == 0)


def part2(data):
    return sum(
        abs((y // 100) - (x // 100))
        + (1 if y % 100 == 0 and x > y else 0)
        - (1 if x % 100 == 0 and x > y else 0)
        for x, y in pairwise(accumulate([50] + data))
    )


def main():
    data = get_data("inputs/day1.txt")
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")

if __name__ == "__main__":
    main()