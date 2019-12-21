PORTAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LEVEL_LIMIT = 25


def find_portals(maze):
    global portals

    for y in range(len(maze) - 1):
        for x in range(len(maze[y]) - 1):
            # Ignore everything except capital letters
            if maze[y][x] in PORTAL_LETTERS:
                # Found the first letter, look for the second
                # It's either to the right, or below
                if maze[y + 1][x] in PORTAL_LETTERS:
                    portal_name = "".join([maze[y][x], maze[y + 1][x]])
                    # The location is either above or below as well
                    if y > 0 and maze[y - 1][x] == ".":
                        location = (x, y - 1)
                    else:
                        location = (x, y + 2)

                elif maze[y][x + 1] in PORTAL_LETTERS:
                    portal_name = "".join([maze[y][x], maze[y][x + 1]])
                    if x > 0 and maze[y][x - 1] == ".":
                        location = (x - 1, y)
                    else:
                        location = (x + 2, y)
                else:
                    # We're looking at a second character, so we can skip
                    portal_name = ""

                if portal_name != "":
                    # Have we already seen this portal?
                    if portal_name in portals.keys():
                        # Append the location
                        portals[portal_name].append(location)
                    else:
                        portals[portal_name] = [location]

    # Order the portals, outer in portals[0], inner in portals[1]
    for portal_name in portals.keys():
        if portal_name == "AA" or portal_name == "ZZ":
            pass
        elif (
            portals[portal_name][1][0] == 2
            or portals[portal_name][1][1] == 2
            or portals[portal_name][1][0] == len(maze[0]) - 4
            or portals[portal_name][1][1] == len(maze) - 3
        ):
            temp = portals[portal_name][1]
            portals[portal_name][1] = portals[portal_name][0]
            portals[portal_name][0] = temp


def find_shortest_path(start, end, steps, maze):

    # Use BFS to find the shortest path to the exit

    next_pos = [(start, 0)]
    seen = set([start])

    while next_pos:
        current = next_pos.pop()
        current_pos = current[0]
        steps = current[1]
        if current_pos == end:
            return steps

        # Are we at a portal?
        for portal in portals.keys():
            # Ignore the start and end
            if portal == "AA" or portal == "ZZ":
                pass

            elif (
                current_pos == portals[portal][0]
                and portals[portal][1] not in seen
            ):
                next_pos.append((portals[portal][1], steps + 1))
                seen.add(current_pos)

            elif (
                current_pos == portals[portal][1]
                and portals[portal][0] not in seen
            ):
                next_pos.append((portals[portal][0], steps + 1))
                seen.add(current_pos)

        # Check everything else around us
        for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            neighbor = (
                current_pos[0] + dir[0],
                current_pos[1] + dir[1],
            )
            if maze[neighbor[1]][neighbor[0]] == "." and neighbor not in seen:
                next_pos.append((neighbor, steps + 1))
                seen.add(neighbor)


def find_shortest_path2(start, end, maze):

    # Use BFS to find the shortest path to the exit

    next_pos = [(start, 0, 0)]
    seen = {}
    seen[0] = set(start)

    while next_pos:
        current = next_pos.pop()
        current_pos = current[0]
        steps = current[1]
        current_level = current[2]

        # Limit the levels
        if current_level > LEVEL_LIMIT:
            continue

        # Create our tracker if it's not there
        if current_level + 1 not in seen.keys():
            seen[current_level + 1] = set()

        # Do we have this maze?
        if current_pos == end and current_level == 0:
            return steps

        # Are we at a portal?
        for portal in portals.keys():
            # Ignore the start and end
            if portal == "AA" or portal == "ZZ":
                pass

            # Ignore outer levels on level 0
            elif (
                current_level > 0
                and current_pos == portals[portal][0]
                and portals[portal][1] not in seen[current_level - 1]
            ):
                next_pos.append(
                    (portals[portal][1], steps + 1, current_level - 1)
                )
                seen[current_level - 1].add(portals[portal][1])

            # Inner portal check
            elif (
                current_pos == portals[portal][1]
                and portals[portal][0] not in seen[current_level + 1]
            ):
                next_pos.append(
                    (portals[portal][0], steps + 1, current_level + 1)
                )
                seen[current_level + 1].add(portals[portal][0])

        # Check everything else around us
        for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            neighbor = (
                current_pos[0] + dir[0],
                current_pos[1] + dir[1],
            )
            if (
                maze[neighbor[1]][neighbor[0]] == "."
                and neighbor not in seen[current_level]
            ):
                next_pos.append((neighbor, steps + 1, current_level))
                seen[current_level].add(neighbor)


if __name__ == "__main__":
    global portals, paths

    maze = []
    portals = {}

    # Read input
    with open("day20/input.txt") as f:
        line = f.readline()
        while line != "":
            maze.append(list(line))
            line = f.readline()

    # Locate all the portals
    find_portals(maze)

    print(f"Maze dimensions: ({len(maze)}, {len(maze[0])})")

    print(f"Portals: {portals}")

    # Find the shortest path
    paths = {}
    paths[portals["AA"][0]] = 0
    visited = set()
    shortest = find_shortest_path(portals["AA"][0], portals["ZZ"][0], 0, maze)
    print(f"Shortest path to ZZ = {shortest}")

    # Part 2
    # Ignore all outer portals on level 0, ignore AA and ZZ on all others
    current_level = 0

    visited = set()
    shortest = find_shortest_path2(portals["AA"][0], portals["ZZ"][0], maze)
    print(f"Shortest path to ZZ = {shortest}")
