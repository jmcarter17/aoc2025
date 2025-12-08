from pathlib import Path

folder = Path(__file__).resolve().parent


def parse_input(file):
    with open(file) as f:
        ranges = f.read().strip().split(",")
        return [tuple(map(int, r.split("-"))) for r in ranges]


def divisors_of(length):
    for i in range(2, length + 1):
        if length % i == 0:
            yield i


def sum_invalids(data, is_invalid):
    return sum(x for (a, b) in data for x in range(a, b + 1) if is_invalid(str(x)))


def part1_naive(data):
    inv = lambda s: s == s[: len(s) // 2] * 2
    return sum_invalids(data, inv)


def part2_naive(data):
    inv = lambda s: any(s == s[: len(s) // k] * k for k in (divisors_of(len(s))))
    return sum_invalids(data, inv)


def generate_invalids(a, b, divisor_filter=None):
    """Generate all invalid IDs in range [a, b].
    Invalid: strings where s == s[:len(s)//k]*k for divisor k > 1 of len(s)

    Args:
        a: Start of range (inclusive)
        b: End of range (inclusive)
        divisor_filter: Optional function to filter which divisors to use.
                       If None, uses all divisors (part2 behavior).
                       For part1, use: lambda k: k == 2
    """
    invalids = set()

    min_len = len(str(a))
    max_len = len(str(b))

    for length in range(min_len, max_len + 1):
        # For each divisor k of length (where k > 1)
        for k in divisors_of(length):
            # Apply filter if provided
            if divisor_filter and not divisor_filter(k):
                continue

            pattern_len = length // k

            # Generate all possible patterns of length pattern_len
            start = 10 ** (pattern_len - 1) if pattern_len > 1 else 0
            end = 10**pattern_len

            for pattern_num in range(start, end):
                pattern_str = str(pattern_num).zfill(pattern_len)
                invalid_str = pattern_str * k
                invalid_num = int(invalid_str)

                if a <= invalid_num <= b:
                    invalids.add(invalid_num)

    return list(invalids)


def part1_optimized(data):
    """Optimized part1: generate invalid IDs where pattern repeats exactly twice (k=2)"""
    return sum(
        sum(generate_invalids(a, b, divisor_filter=lambda k: k == 2)) for a, b in data
    )


def part2_optimized(data):
    """Optimized part2: generate invalid IDs for all divisors (k > 1)"""
    return sum(sum(generate_invalids(a, b)) for a, b in data)


def main():
    data = parse_input(folder / "input.txt")
    # print(f"part1: {part1_naive(data)}")
    # print(f"part2: {part2_naive(data)}")
    print(f"part1_optimized: {part1_optimized(data)}")
    print(f"part2_optimized: {part2_optimized(data)}")


def test_part1():
    data = parse_input(folder / "test_input.txt")
    assert part1_naive(data) == 1227775554


def test_part2():
    data = parse_input(folder / "test_input.txt")
    assert part2_naive(data) == 4174379265


def test_part1_optimized():
    data = parse_input(folder / "test_input.txt")
    assert part1_optimized(data) == 1227775554


def test_part2_optimized():
    data = parse_input(folder / "test_input.txt")
    assert part2_optimized(data) == 4174379265


def test_optimized_matches_original():
    """Verify optimized solutions match original solutions"""
    data = parse_input(folder / "test_input.txt")
    assert part1_naive(data) == part1_optimized(data)
    assert part2_naive(data) == part2_optimized(data)


if __name__ == "__main__":
    main()
