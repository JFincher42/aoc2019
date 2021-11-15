from typing import List
from pprint import pprint


def build_graph(lines):
    # First, find the start
    for y, line in enumerate(lines):
        if "@" in line:
            x = line.index("@")
            start = (x, y)
            break
    pprint(start)


if __name__ == "__main__":

    maze = []
    # Read input
    with open("sample1.txt") as f:
        maze = [line for line in f.readlines()]

    # Build a graph of the paths from the maze
    graph = build_graph(maze)
