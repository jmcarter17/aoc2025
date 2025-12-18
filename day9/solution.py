from itertools import combinations, pairwise, chain
from pathlib import Path

from matplotlib import pyplot as plt
from shapely import box
from shapely.geometry import Polygon
from shapely.plotting import plot_polygon
from shapely.prepared import prep

from utilities.timer import timer


def parse_input(file):
    with open(file) as f:
        data = [list(map(int, line.strip().split(","))) for line in f]
        return data

def calc_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

@timer
def part1(data):
    return max(calc_area(p1, p2) for p1, p2 in combinations(data, 2))

def normalize_pair(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int, int, int]:
    """Convert two points into a normalized edge tuple (min_x, min_y, max_x, max_y)."""
    # minx, miny = min(p1[0], p2[0]), min(p1[1], p2[1])
    return (
        min(p1[0], p2[0]),
        min(p1[1], p2[1]),
        max(p1[0], p2[0]),
        max(p1[1], p2[1]),
    )

def get_normalized_edges(tiles: list[tuple[int, int]]) -> list[tuple[int, int, int, int]]:
    """Convert tiles into a list of normalized edge tuples (min_x, min_y, max_x, max_y)."""
    return [
        normalize_pair(p1, p2)
        for p1, p2 in pairwise(tiles + [tiles[0]])
    ]


def is_fully_contained(
    edges: list[tuple[int, int, int, int]],
    min_x: int,
    min_y: int,
    max_x: int,
    max_y: int,
) -> bool:
    """Check if the rectangle is fully contained.
    1. For each edge, check if the rectangle does not cross any edge."""
    # return all(
    #     min_x >= e_max_x or max_x <= e_min_x or min_y >= e_max_y or max_y <= e_min_y
    #     for e_min_x, e_min_y, e_max_x, e_max_y in edges
    # )
    return not any(
        min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y
        for e_min_x, e_min_y, e_max_x, e_max_y in edges
    )

@timer
def part2(data) -> int:
    """Find the largest rectangle fully contained within the polygon."""
    edges = get_normalized_edges(data)
    result = 0

    for p1, p2 in combinations(data, 2):
        area = calc_area(p1, p2)
        if area <= result:
            continue

        min_x, min_y, max_x, max_y = normalize_pair(p1, p2)
        if is_fully_contained(edges, min_x, min_y, max_x, max_y):
            result = area

    return result

@timer
def part2_withlib(data):
    """First create a polygon from al the points in the data,
    then from all pairs of points, calculate the area of the rectangle
    they form and check if all other points are inside that rectangle.
    Find max area of such rectangles."""
    polygon = Polygon(data)
    prepared_polygon = prep(polygon)

    max_area = 0
    for p1, p2 in combinations(data, 2):
        area = calc_area(p1, p2)
        if area <= max_area:
            continue
        rectangle = box(
            min(p1[0], p2[0]), min(p1[1], p2[1]),
            max(p1[0], p2[0]), max(p1[1], p2[1])
        )
        if prepared_polygon.contains(rectangle):
            max_area = area
    return max_area


def plot_data(data):
    polygon = Polygon(data)
    plot_polygon(polygon)
    plt.axis("equal")
    plt.show()


def main():
    folder = Path(__file__).resolve().parent
    data = parse_input(folder / "input.txt")
    part1(data)
    part2(data)
    part2_withlib(data)
    # plot_data(data)


if __name__ == "__main__":
    main()
