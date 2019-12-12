from functools import reduce


def get_vel(diff):
    if diff == 0:
        return 0
    return abs(diff) / diff


def get_energy(position, velocity):
    pot, kin = 0, 0
    for axis in range(3):
        pot += abs(position[axis])
        kin += abs(velocity[axis])
    return pot * kin


if __name__ == "__main__":

    moons_position = []

    with open("day12/input.txt") as f:
        line = f.readline().strip()
        while line != "":
            raw_coords = line[1:-1].split(",")
            position = []
            for raw_coord in raw_coords:
                axis = raw_coord.split("=")
                position.append(int(axis[1]))
            moons_position.append(position)
            line = f.readline().strip()

    num_moons = len(moons_position)
    moons_velocity = [[0 for x in range(3)] for y in range(num_moons)]
    moons_energy = [0 for y in range(num_moons)]

    # Part 1

    # 1000 steps
    for step in range(1000):
        # Visit every moon
        for moon in range(num_moons):
            # Visit the rest of the moons
            for next_moon in range(moon + 1, num_moons):
                # Get the velocity change
                for axis in range(3):
                    moons_velocity[moon][axis] += get_vel(
                        moons_position[next_moon][axis]
                        - moons_position[moon][axis]
                    )
                    moons_velocity[next_moon][axis] += get_vel(
                        moons_position[moon][axis]
                        - moons_position[next_moon][axis]
                    )

        # Now change the positions
        for moon in range(num_moons):
            for axis in range(3):
                moons_position[moon][axis] += moons_velocity[moon][axis]

            # Now figure out the energy
            moons_energy[moon] = get_energy(
                moons_position[moon], moons_velocity[moon]
            )

    print(f"Total energy: {reduce(lambda x, y: x+y, moons_energy)}")
