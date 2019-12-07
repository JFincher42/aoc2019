from intcode import intcode

if __name__ == "__main__":

    # Read input
    with open("day05/input.txt") as f:
        memory = [int(x) for x in f.readline().split(",")]

    intcode(memory)
