from intcode import IntCode
from sys import setrecursionlimit
from collections import defaultdict

direction_delta = [(x, y) for x, y in zip([0, 0, 0, -1, 1], [0, -1, 1, 0, 0])]
reverse = {d: r for d, r in zip([1, 2, 3, 4], [2, 1, 4, 3])}
WALL, EMPTY, O2 = range(1, 4)

current_pos = (0, 0)
o2_pos = (0, 0)
maze = defaultdict(int)


def next_pos(pos, direction):
    return (
        pos[0] + direction_delta[direction][0],
        pos[1] + direction_delta[direction][1],
    )


def find_o2_tank(direction=0):

    global intcode, maze, current_pos, o2_pos

    for d in range(1, 5):
        new_pos = next_pos(current_pos, d)

        # Have we already looked in this direction
        if new_pos not in maze.keys():

            # Check this direction
            intcode.write_input(d)
            intcode.run()
            maze[new_pos] = int(intcode.read_output()) + 1

            if maze[new_pos] == O2:
                o2_pos = new_pos
            if maze[new_pos] != 1:
                current_pos = new_pos
                find_o2_tank(d)

    if current_pos != (0, 0):
        intcode.write_input(reverse[direction])
        intcode.run()
        _ = int(intcode.read_output())
        current_pos = next_pos(current_pos, reverse[direction])


def find_shortest_path(start, dest, steps, maze):
    global paths, visited

    if start in visited:
        return

    paths[start] = min(paths[start], steps)
    visited.append(start)

    # if start == dest:
    #     return

    current = start
    for d in range(1, 5):
        neighbor = next_pos(current, d)
        if neighbor in paths.keys() and neighbor not in visited:
            find_shortest_path(neighbor, dest, steps + 1, maze)


if __name__ == "__main__":
    global intcode, paths, visited

    # Read input
    memory = []
    with open("day15/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    # Create new IntCode instance
    intcode = IntCode(memory, 0)

    # maze = {}
    maze[(0, 0)] = EMPTY
    setrecursionlimit(50000)
    find_o2_tank()

    print(f"O2 Tank at {o2_pos}")

    paths = {k: 1_000_000 for k in maze.keys() if maze[k] != WALL}
    paths[0, 0] = 0
    visited = []

    find_shortest_path((0, 0), o2_pos, 0, maze)
    print(f"Shortest path = {paths[o2_pos]}")

    paths = {k: 1_000_000 for k in maze.keys() if maze[k] != WALL}
    paths[0, 0] = 0
    visited = []

    find_shortest_path(o2_pos, (0, 0), 0, maze)
    path_lengths = list(paths.values())
    path_lengths.sort()
    print(f"Time = {path_lengths[len(path_lengths)-1]}")
