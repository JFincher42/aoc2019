from typing import List, DefaultDict
import collections


def part1():
    pass


def part2():
    pass


def plot_path(path: List):

    # We'll create a dictionary of the grid locations the path covers

    # Empty list to start
    panel = []

    # Start at (0,0)
    pos_x, pos_y = 0, 0

    # Look at every trace in the path
    for trace in path:

        # Which direction are we moving?
        if trace[0] == "U":  # Up
            # Y value goes up
            panel.extend(
                [(pos_x, y) for y in range(pos_y + 1, pos_y + trace[1] + 1)]
            )
            pos_y += trace[1]

        elif trace[0] == "D":  # Down
            # Y value does down
            panel.extend(
                [
                    (pos_x, y)
                    for y in range(pos_y - 1, pos_y - trace[1] - 1, -1)
                ]
            )
            pos_y -= trace[1]

        elif trace[0] == "R":  # Right
            # X value goes up
            panel.extend(
                [(x, pos_y) for x in range(pos_x + 1, pos_x + trace[1] + 1)]
            )
            pos_x += trace[1]

        elif trace[0] == "L":  # Left
            # X value does down
            panel.extend(
                [
                    (x, pos_y)
                    for x in range(pos_x - 1, pos_x - trace[1] - 1, -1)
                ]
            )
            pos_x -= trace[1]

    return panel


def find_intersections(panel: List, path: List):
    # We do roughly the same thing as above, but we only create a list of intersections

    # Empty list to start
    intersections = []

    # Start at (0,0)
    pos_x, pos_y = 0, 0

    # Look at every trace in the path
    for trace in path:

        # Which direction are we moving?
        if trace[0] == "U":  # Up
            # Y value goes up
            trace_grid = [
                (pos_x, y) for y in range(pos_y + 1, pos_y + trace[1] + 1)
            ]

            pos_y += trace[1]

        elif trace[0] == "D":  # Down
            # Y value does down
            trace_grid = [
                (pos_x, y) for y in range(pos_y - 1, pos_y - trace[1] - 1, -1)
            ]

            pos_y -= trace[1]

        elif trace[0] == "R":  # Right
            # X value goes up
            trace_grid = [
                (x, pos_y) for x in range(pos_x + 1, pos_x + trace[1] + 1)
            ]

            pos_x += trace[1]

        elif trace[0] == "L":  # Left
            # X value does down
            trace_grid = [
                (x, pos_y) for x in range(pos_x - 1, pos_x - trace[1] - 1, -1)
            ]

            pos_x -= trace[1]

        # Track the intersections
        for trace_location in trace_grid:
            if trace_location in panel:
                intersections.append(trace_location)

    return intersections


if __name__ == "__main__":

    # Read input, parse direction and distance into a tuple
    with open("day03/input.txt") as f:
        path1 = [(x[0], int(x[1:])) for x in f.readline().split(",")]
        path2 = [(x[0], int(x[1:])) for x in f.readline().split(",")]

    print(f"Path 1, length {len(path1)}")
    print(f"Path 2, length {len(path2)}")

    # Plot both paths separately
    panel1 = plot_path(path1)
    # print(f"Panel 1, length {len(panel1)}")
    panel2 = plot_path(path2)
    # print(f"Panel 2, length {len(panel2)}")

    # Create a dictionary to hold the intersections
    # Key is the tuple path, value is the path in that location
    intersections = collections.defaultdict(list)
    for location in panel1:
        intersections[location].append(1)
    for location in panel2:
        intersections[location].append(2)

    # Calculate a list of manhattan distances for every intersection
    # Intersections are dictionary entries where the value is [1,2]
    manhattan = [
        abs(x) + abs(y)
        for (x, y) in intersections
        if intersections[(x, y)] == [1, 2]
    ]

    # Print the minimum distance
    print(f"Manhattan: {min(manhattan)}")
