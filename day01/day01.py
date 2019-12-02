def part1():

    # Initialize cumulative sum
    sum = 0
    # Read input
    with open("day01/input.txt") as f:
        line = f.readline()
        while line != "":
            # Get the mass
            mass = int(line)

            # Calculate fuel and total
            fuel = (mass // 3) - 2
            sum += fuel

            # Get next line
            line = f.readline()

    print(f"Part 1: Total Fuel: {sum}")


def part2():

    # Initialize cumulative sum
    sum = 0
    # Read input
    with open("day01/input.txt") as f:
        line = f.readline()
        while line != "":

            # Init cumulative fuel
            fuel_sum = 0

            # Get the mass
            mass = int(line)

            # Calculate fuel
            fuel = (mass // 3) - 2

            # Add it to the total
            fuel_sum += fuel

            # Figure out the fuel for the fuel
            while fuel > 0:
                fuel = (fuel // 3) - 2
                if fuel < 0:
                    fuel = 0
                fuel_sum += fuel

            # Sum up the total fule needed
            sum += fuel_sum

            # Get next line
            line = f.readline()

    print(f"Part 2: Total Fuel: {sum}")


if __name__ == "__main__":
    part1()
    part2()
