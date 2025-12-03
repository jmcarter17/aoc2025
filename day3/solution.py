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

    return int(''.join(map(str, stack[:n])))


# def max_joltage_old(row):
#     x = max(row)
#     i = row.index(x)
#     if i == len(row) - 1:
#         y = max(row[:i])
#         joltage = y*10 + x
#     else:
#         y = max(row[i+1:])
#         joltage = x*10 + y
#     return joltage


def part1(data):
    return sum(max_joltage(row, 2) for row in data)


def part2(data):
    return sum(max_joltage(row, 12) for row in data)


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    # print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")

if __name__ == "__main__":
    main()