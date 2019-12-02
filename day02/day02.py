from typing import List


def intcode(memory: List):

    # Setup the computer
    ip = 0

    # Run the program
    while ip < len(memory) and memory[ip] != 99:
        # Add the two numbers
        if memory[ip] == 1:
            memory[memory[ip + 3]] = (
                memory[memory[ip + 1]] + memory[memory[ip + 2]]
            )
            # Where is the next IP?
            next_ip = 4

        # Multiply the two numbers
        elif memory[ip] == 2:
            memory[memory[ip + 3]] = (
                memory[memory[ip + 1]] * memory[memory[ip + 2]]
            )
            # Where is the next IP?
            next_ip = 4

        # Something has gone horribly wrong.
        else:
            # print("SYNTAX ERROR")
            break

        ip += next_ip


def part1(memory: List, noun: int, verb: int):

    # Do the swap
    memory[1] = noun
    memory[2] = verb

    # Run the program
    intcode(memory)

    return memory[0]


def part2(memory):

    # Check every noun between 0 and 99
    for noun in range(100):
        # Check every verb between 0 and 99
        for verb in range(100):

            # Need to clean memory every time
            clean_memory = memory.copy()

            # Look for our specific answer
            if 19690720 == part1(clean_memory, noun, verb):
                return (noun, verb)

    # If we get here, we've failed
    return (0, 0)


if __name__ == "__main__":

    # Read input
    with open("day02/input.txt") as f:
        memory = [int(x) for x in f.readline().split(",")]

    # Start with a clean slate
    clean_memory = memory.copy()

    # Part 1
    print(f"Part 1: memory[0] =  {part1(clean_memory, 12, 2)}")

    # Clean slate again for Part 2
    clean_memory = memory.copy()

    # Part 2 returns a tuple, which we process
    noun, verb = part2(clean_memory)
    print(
        f"Part 2: (Noun, Verb) = ({noun}, {verb}), product = {100*noun + verb}"
    )
