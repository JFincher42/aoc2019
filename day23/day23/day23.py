from pprint import pprint
import pathlib
from intcode import IntCode

root_path = pathlib.Path.home() / "git" / "aoc2019" / "day23"


def part1():
    return -1


def part2(lines):

    return -1


if __name__ == "__main__":

    memory = []
    with open(root_path / "input", "r") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    # Create 50 IntCode computers
    network = []
    for i in range(50):
        icpc = IntCode(memory[:], 0)
        icpc.write_input(str(i))
        network.append(icpc)

    # Now we can kick them all off
    finished = False
    current = 0
    while not finished:
        print(f"Running #{current}")
        network[current].run()
        dest = network[current].read_output()
        if dest != "":
            network[current].run()
            x = network[current].read_output()
            network[current].run()
            y = network[current].read_output()
            print(f"  Paused, output is {dest}, {x}, {y}")
            if dest == "255":
                finished = True
                print(f"Part 1: Answer: {y}")
            else:
                network[int(dest)].write_input(x)
                network[int(dest)].write_input(y)
        current = (current + 1) % 50
        # current = int(dest)

    print(f"Part 2: Answer: {part2()}")
