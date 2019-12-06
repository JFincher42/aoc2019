def count_bodies(planets, orbits, level):
    count = level * len(planets)
    for body in planets:
        if body in orbits:
            count += count_bodies(orbits[body], orbits, level + 1)

    return count


def find_route(orbits, start, end):
    route = []
    if start not in orbits:
        return route

    elif end in orbits[start]:
        return [start]

    else:
        for body in orbits[start]:
            temp = find_route(orbits, body, end)
            if len(temp) > 0:
                route.append(start)
                route.extend(temp)

    return route

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

    # Part 2: First, figure out where each of us is

    for k,v in orbits.items():
        if "YOU" in v:
            my_loc = k
        if "SAN" in v:
            san_loc = k

    # Find my path to COM
    my_path = find_route(orbits, 'COM', my_loc)
    san_path = find_route(orbits, 'COM', san_loc)
    my_path.append(my_loc)
    san_path.append(san_loc)

    # Find the first common point
    # Reverse them to make it easier
    my_path.reverse()
    san_path.reverse()

    my_path_count = 0
    # First, find the point in my location list
    for body in my_path:
        if body in san_path:
            common = body
            break
        else:
            my_path_count += 1


    # Now count the items between them
    san_path_count = 0
    for body in san_path:
        if body == common:
            break
        else:
            san_path_count+=1


    print(f"   My Location and Path:{my_loc} and {my_path}")
    print(f"Santa Location and Path:{san_loc} and {san_path}")
    print(f"Orbital transfers required = {my_path_count + san_path_count}")