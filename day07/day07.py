from typing import Tuple
from intcode import IntCode
import sys
import io
from contextlib import redirect_stdout
import itertools


def run_test(phases: Tuple, init_strength: int):

    strength = str(init_strength)

    # Loop through phases given
    for phase in phases:

        intcode = IntCode(memory, 0)
        intcode.write_input(phase)
        intcode.write_input(strength)
        intcode.run()
        strength = int(intcode.read_output())

    # Return the output strength
    return int(strength)


def all_halted(amps):
    return (
        amps[0].is_halted()
        and amps[1].is_halted()
        and amps[2].is_halted()
        and amps[3].is_halted()
        and amps[4].is_halted()
    )


def run_test_loop(amplifiers: list, phases: Tuple, init_strength: int):

    strength = str(init_strength)
    current_phase = 0

    # Current amp
    amp = 0

    # keep going until all amplifiers are halted
    while not all_halted(amplifiers):
        # Get current phase, if any
        if current_phase < len(phases):
            amplifiers[amp].write_input(phases[current_phase])
            current_phase += 1

        # Run the program with the proper input
        amplifiers[amp].write_input(strength)
        amplifiers[amp].run()
        strength = amplifiers[amp].read_output()

        # Next amp
        amp = (amp + 1) % 5

    # Return the output strength
    return int(strength)


if __name__ == "__main__":

    # Read input
    with open("day07/input.txt") as f:
        memory = [int(x) for x in f.readline().split(",")]

    # Set our current max strength
    max_strength = 0

    # Loop through all our possible permutations
    for phase in itertools.permutations("01234", 5):
        strength = run_test(phase, 0)
        if strength > max_strength:
            max_strength = strength

    print(f"Part 1 Final: {max_strength}")

    # Part 2: New problem, same file, but need it fresh
    with open("day07/input.txt") as f:
        memory = [int(x) for x in f.readline().split(",")]

    # Set our current max strength
    max_strength = 0

    # Loop through all our possible permutations
    for phase in itertools.permutations("56789", 5):

        # Init five different amplifiers
        amplifiers = []
        for _ in range(5):
            amplifiers.append(IntCode(memory, 0))

        strength = run_test_loop(amplifiers, phase, 0)
        if strength > max_strength:
            max_strength = strength

    print(f"Part 2 Final: {max_strength}")
