# AOC 2019 Day 24

import pathlib
import math
from pprint import pprint
from copy import deepcopy

root_path = pathlib.Path.home() / "git" / "aoc2019" / "day24"

def calc_biodiversity(grid):
    biodiversity = 0
    bin = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                biodiversity += int(math.pow(2, bin))
            bin += 1
    return biodiversity

def neighbors(grid, i, j, char):

    offsets = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    count = 0
    for offset in offsets:
        if (offset[0] >= 0 and offset[0] <= 4 and offset[1] >= 0 and offset[1] <= 4):
            if grid[offset[0]][offset[1]] == char:
                count += 1
    return count


def infest(grid):
    # new_grid = [["."]*5]*5
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # new_grid[i][j] = grid[i][j]
            if grid[i][j] == "#" and neighbors(grid, i, j, "#") != 1:
                new_grid[i][j]="."
            if grid[i][j] == "." and neighbors(grid, i, j, "#") in (1, 2):
                new_grid[i][j] = "#"
    return new_grid
    

def part1(grid):
    patterns = set()
    biod = calc_biodiversity(grid)
    while biod not in patterns:
        patterns.add(biod)
        grid = infest(grid)
        biod = calc_biodiversity(grid)
    pprint(grid)
    return biod

def part2(lines):
    return -1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    grid = [[ch for ch in line] for line in lines]

    print(f"Part 1: Answer: {part1(grid)}")
    print(f"Part 2: Answer: {part2(lines)}")
