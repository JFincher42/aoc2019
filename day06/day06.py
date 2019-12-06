def count_bodies(planets, orbits, level):
    count = level * len(planets)
    for body in planets:
        if body in orbits:
            count += count_bodies(orbits[body], orbits, level + 1)

    return count


if __name__ == "__main__":

    # Open the file, process into dict
    orbits = {}

    # Read input
    with open("day06/input.txt") as f:
        line = f.readline()
        while line:
            k, v = line.strip().split(")")

            # More than one object can orbit another
            if k in orbits:
                orbits[k].append(v)
            else:
                orbits[k] = [v]

            line = f.readline()

    # Part 1: Find the root node, and start counting
    level = 2
    count = len(orbits["COM"])

    for body in orbits["COM"]:
        count += count_bodies(orbits[body], orbits, level)

    print(f"# of Orbits = {count}")
