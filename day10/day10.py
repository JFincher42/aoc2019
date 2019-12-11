import math
from collections import defaultdict


def count_visible(map, x_start, y_start):
    if map[y_start][x_start] == ".":
        return {}

    count = defaultdict(int)

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "#":
                dx = x - x_start
                dy = y - y_start
                common = math.gcd(dx, dy)
                if common != 0:
                    count[(dx // common, dy // common)] += 1
                else:
                    count[(dx, dy)] += 1

    return count


if __name__ == "__main__":
    map = []
    with open("day10/input.txt") as f:
        for line in f.readlines():
            map.append(list(line.strip()))

    max_asteroids = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            current_map = count_visible(map, x, y)
            num_asteroids = len(current_map) - 1
            if num_asteroids > max_asteroids:
                max_asteroids = max(max_asteroids, num_asteroids)
                asteroid_map = current_map.copy()
                station_x, station_y = x, y

    print(f"Part 1: Maximum asteroids seen: {max_asteroids}")

    # Part 2
