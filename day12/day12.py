from functools import reduce
from copy import deepcopy
import math


def get_vel(diff):
    if diff == 0:
        return 0
    return int(abs(diff) / diff)


def get_energy(position, velocity):
    pot, kin = 0, 0
    for axis in range(3):
        pot += abs(position[axis])
        kin += abs(velocity[axis])
    return pot * kin


def find_position(zero_pos, current_pos):
    for position in zero_pos:
        if position == current_pos:
            return True

    zero_pos.append(deepcopy(current_pos))
    print(f"added {zero_pos}")
    return False


def factorize(n):

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    divisor = 3

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 2
    return factors


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
    # for step in range(10):
    #     # Visit every moon
    #     for moon in range(num_moons):
    #         # Visit the rest of the moons
    #         for next_moon in range(moon + 1, num_moons):
    #             # Get the velocity change
    #             for axis in range(3):
    #                 moons_velocity[moon][axis] += get_vel(
    #                     moons_position[next_moon][axis]
    #                     - moons_position[moon][axis]
    #                 )
    #                 moons_velocity[next_moon][axis] += get_vel(
    #                     moons_position[moon][axis]
    #                     - moons_position[next_moon][axis]
    #                 )

    #     # Now change the positions
    #     for moon in range(num_moons):
    #         for axis in range(3):
    #             moons_position[moon][axis] += moons_velocity[moon][axis]

    #         # Now figure out the energy
    #         moons_energy[moon] = get_energy(
    #             moons_position[moon], moons_velocity[moon]
    #         )

    # print(f"Total energy: {reduce(lambda x, y: x+y, moons_energy)}")

    # Part 2

    # Store out initial zero position
    zero_position = deepcopy(moons_position)

    x_repeat, y_repeat, z_repeat = 0, 0, 0
    step = 0
    while x_repeat == 0 or y_repeat == 0 or z_repeat == 0:
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

        step += 1

        # Check for repeats
        # X, Y, Z
        found = [True, True, True]
        for moon in range(num_moons):
            for axis in range(3):
                found[axis] = found[axis] and (
                    (moons_position[moon][axis], moons_velocity[moon][axis])
                    == (zero_position[moon][axis], 0)
                )
        if found[0] and x_repeat == 0:
            x_repeat = step
        if found[1] and y_repeat == 0:
            y_repeat = step
        if found[2] and z_repeat == 0:
            z_repeat = step

    print(f"Repeats: x={x_repeat}, y={y_repeat}, z={z_repeat}")
    print(f"X factors = {factorize(x_repeat)}")
    print(f"Y factors = {factorize(y_repeat)}")
    print(f"Z factors = {factorize(z_repeat)}")
