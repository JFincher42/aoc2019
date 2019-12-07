from typing import Tuple
from intcode import intcode
import sys
import io
from contextlib import redirect_stdout
import itertools


def run_test(phases: Tuple, init_strength: int):

    strength = str(init_strength)

    # Loop through phases given
    for phase in phases:
        # Redirect output to a new buffere
        out_bytes = io.BytesIO()
        out_buf = io.TextIOWrapper(
            out_bytes,
            sys.stdout.encoding,
            line_buffering=True,
            write_through=True,
        )

        # Run the program with the proper input
        with redirect_stdout(out_buf):
            sys.stdin = io.StringIO(phase + "\n" + strength + "\n")
            intcode(memory)

            # Get the output strength
            out_buf.seek(0)
            strength = out_buf.readline().strip()

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

    #
