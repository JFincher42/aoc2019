import string

from string import ascii_lowercase


def find_location(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "@":
                return x, y


def map_extents(paths, steps, x, y) -> dict:
    extents = {}
    found_door = False
    # Check north
    if y > 1:
        # Found a door or a key
        if paths[y - 1][x] in string.ascii_letters:
            found_door = paths[y - 1][x] in string.ascii_uppercase

            # Have we seen it already?
            if paths[y - 1][x] in extents.keys():
                # Is this a shorter path?
                if extents[paths[y - 1][x]] > steps + 1:
                    extents[paths[y - 1][x]] = steps + 1
            else:
                extents[paths[y - 1][x]] = steps + 1

            if found_door:
                return extents
        # Open area
        elif paths[y - 1][x] == ".":
            extents.update(map_extents(paths, steps + 1, x, y - 1))

    # Check south
    if y < len(paths) - 2:
        # Found a door or a key
        if paths[y + 1][x] in string.ascii_letters:
            found_door = paths[y + 1][x] in string.ascii_uppercase
            # Have we seen it already?
            if paths[y + 1][x] in extents.keys():
                # Is this a shorter path?
                if extents[paths[y + 1][x]] > steps + 1:
                    extents[paths[y + 1][x]] = steps + 1
            else:
                extents[paths[y + 1][x]] = steps + 1

            if found_door:
                return extents

        # Open area
        elif paths[y + 1][x] == ".":
            extents.update(map_extents(paths, steps + 1, x, y + 1))

    # Check west
    if x > 1:
        # Found a door or a key
        if paths[y][x - 1] in string.ascii_letters:
            found_door = paths[y][x - 1] in string.ascii_uppercase
            # Have we seen it already?
            if paths[y][x - 1] in extents.keys():
                # Is this a shorter path?
                if extents[paths[y][x - 1]] > steps + 1:
                    extents[paths[y][x - 1]] = steps + 1
            else:
                extents[paths[y][x - 1]] = steps + 1

            if found_door:
                return extents

        # Open area
        elif paths[y][x - 1] == ".":
            extents.update(map_extents(paths, steps + 1, x - 1, y))

    if x < len(paths[y]) - 2:
        # Found a door or a key
        if paths[y][x + 1] in string.ascii_letters:
            found_door = paths[y][x + 1] in string.ascii_uppercase
            # Have we seen it already?
            if paths[y][x + 1] in extents.keys():
                # Is this a shorter path?
                if extents[paths[y][x + 1]] > steps + 1:
                    extents[paths[y][x + 1]] = steps + 1
            else:
                extents[paths[y][x + 1]] = steps + 1

            if found_door:
                return extents

        # Open area
        elif paths[y][x + 1] == ".":
            extents.update(map_extents(paths, steps + 1, x + 1, y))

    return extents


if __name__ == "__main__":

    maze = []
    # Read input
    with open("day18/sample1.txt") as f:
        line = f.readline().strip()
        while line != "":
            maze.append(list(line))
            line = f.readline().strip()

    maze_keys = {sq for l in maze for sq in l if sq not in [".", "@", "#"] and sq == sq.lower()}
    pos = [(x, y) for y, l in enumerate(maze) for x, _ in enumerate(l) if _ == "@"]
    x_loc, y_loc = pos[0]

    print(f"Location: ({x_loc}, {y_loc})")
    print(f"Maze keys = {maze_keys}")

    paths = maze.copy()
    steps = 0
    current_extents = map_extents(paths, steps, x_loc, y_loc)
    while len(maze_keys) > 0:
        key_list = [x for x in list(current_extents) if x in string.ascii_lowercase]
        key_list.sort()
        shortest_path = current_extents[key_list[0]]
        for key in key_list:
            if current_extents[key] < shortest_path:
                closest_key = key
        # Go to the closest key




    print(f"Extents: {current_extents}")
