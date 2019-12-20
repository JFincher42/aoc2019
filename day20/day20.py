PORTAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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


if __name__ == "__main__":
    global portals, paths, visited

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

    print(f"Portals: {portals}")

    # Find the shortest path
    paths = {}
    paths[portals["AA"][0]] = 0
    visited = set()
    shortest = find_shortest_path(portals["AA"][0], portals["ZZ"][0], 0, maze)
    print(f"Shortest path to ZZ = {shortest}")
