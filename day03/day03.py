from typing import List
import collections


def plot_path_dist(path: List):

    # Empty list to start
    panel = []

    # Start at (0,0) with distance 0
    pos_x, pos_y, distance = 0, 0, 0

    # Look at every trace in the path
    for trace in path:

        # Which direction are we moving?
        if trace[0] == "U":  # Up
            # Y value goes up
            panel.extend(
                [
                    (pos_x, y, distance + abs(y - pos_y))
                    for y in range(pos_y + 1, pos_y + trace[1] + 1)
                ]
            )
            pos_y += trace[1]
            distance += trace[1]

        elif trace[0] == "D":  # Down
            # Y value does down
            panel.extend(
                [
                    (pos_x, y, distance + abs(y - pos_y))
                    for y in range(pos_y - 1, pos_y - trace[1] - 1, -1)
                ]
            )
            pos_y -= trace[1]
            distance += trace[1]

        elif trace[0] == "R":  # Right
            # X value goes up
            panel.extend(
                [
                    (x, pos_y, distance + abs(x - pos_x))
                    for x in range(pos_x + 1, pos_x + trace[1] + 1)
                ]
            )
            pos_x += trace[1]
            distance += trace[1]

        elif trace[0] == "L":  # Left
            # X value does down
            panel.extend(
                [
                    (x, pos_y, distance + abs(x - pos_x))
                    for x in range(pos_x - 1, pos_x - trace[1] - 1, -1)
                ]
            )
            pos_x -= trace[1]
            distance += trace[1]

    return panel


if __name__ == "__main__":

    # Read input, parse direction and distance into a tuple
    with open("day03/input.txt") as f:
        path1 = [(x[0], int(x[1:])) for x in f.readline().split(",")]
        path2 = [(x[0], int(x[1:])) for x in f.readline().split(",")]

    print(f"Path 1, length {len(path1)}")
    print(f"Path 2, length {len(path2)}")

    # Plot both paths separately
    panel1 = plot_path_dist(path1)
    panel2 = plot_path_dist(path2)

    # Normalize the paths in dictionaries
    dict_panel1 = collections.defaultdict(list)
    for location in panel1:
        dict_panel1[location[0], location[1]].append(location[2])
    dict_panel2 = collections.defaultdict(list)
    for location in panel2:
        dict_panel2[location[0], location[1]].append(location[2])

    # Create a dictionary to hold the intersections
    # Key is the tuple path, value is the path in that location
    intersections = collections.defaultdict(list)
    for k, v in dict_panel1.items():
        intersections[k].append(min(v))
    for k, v in dict_panel2.items():
        intersections[k].append(min(v))

    # Calculate a list of manhattan distances for every intersection
    # Intersections are dictionary entries where the value has two entries
    manhattan = [
        abs(k[0]) + abs(k[1]) for k, v in intersections.items() if len(v) == 2
    ]

    # Print the minimum distance
    print(f"Manhattan: {min(manhattan)}")

    # Part 2

    shortest = [
        abs(v[0]) + abs(v[1]) for k, v in intersections.items() if len(v) == 2
    ]

    print(f"Shortest path: {min(shortest)}")
