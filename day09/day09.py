from intcode import IntCode

if __name__ == "__main__":

    # Read input
    memory = []
    with open("day09/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    # Create new IntCode instance
    intcode = IntCode(memory, 0)
    # Part 1
    # intcode.write_input("1")
    # Part 2
    intcode.write_input("2")

    while not intcode.is_halted():
        intcode.run()
        print(f"{intcode.read_output()}")
