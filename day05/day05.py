from typing import List


def opcode_00():
    print("ERROR")


# Add two numbers
def opcode_01(memory: list, ip: int, modes: str):

    # Get the parameters
    if modes[2] == "0":
        param1 = memory[memory[ip + 1]]
    else:
        param1 = memory[ip + 1]

    if modes[1] == "0":
        param2 = memory[memory[ip + 2]]
    else:
        param2 = memory[ip + 2]

    # Third parameter is always 0
    memory[memory[ip + 3]] = param1 + param2

    # Where is the next IP?
    return ip + 4


# Multiple two numbers
def opcode_02(memory: list, ip: int, modes: str):

    # Get the parameters
    if modes[2] == "0":
        param1 = memory[memory[ip + 1]]
    else:
        param1 = memory[ip + 1]

    if modes[1] == "0":
        param2 = memory[memory[ip + 2]]
    else:
        param2 = memory[ip + 2]

    memory[memory[ip + 3]] = param1 * param2

    # Where is the next IP?
    return ip + 4


# Get user input
def opcode_03(memory: list, ip: int, modes: str):

    # Get user input
    user_input = int(input("INPUT: "))

    if modes[2] == "0":
        memory[memory[ip + 1]] = user_input
    else:
        memory[ip + 1] = user_input

    return ip + 2


# Print output
def opcode_04(memory: list, ip: int, modes: str):

    # Get parameteres
    if modes[2] == "0":
        print(f"OUTPUT: {memory[memory[ip + 1]]}")
    else:
        print(f"OUTPUT: {memory[ip + 1]}")

    return ip + 2


# Jump if true
def opcode_05(memory: list, ip: int, modes: str):

    # Get the parameters
    if modes[2] == "0":
        param1 = memory[memory[ip + 1]]
    else:
        param1 = memory[ip + 1]

    if modes[1] == "0":
        param2 = memory[memory[ip + 2]]
    else:
        param2 = memory[ip + 2]

    if param1 != 0:
        ip = param2
    else:
        ip += 3

    return ip


# Jump if false
def opcode_06(memory: list, ip: int, modes: str):

    # Get the parameters
    if modes[2] == "0":
        param1 = memory[memory[ip + 1]]
    else:
        param1 = memory[ip + 1]

    if modes[1] == "0":
        param2 = memory[memory[ip + 2]]
    else:
        param2 = memory[ip + 2]

    if param1 == 0:
        ip = param2
    else:
        ip += 3

    return ip


# Less than
def opcode_07(memory: list, ip: int, modes: str):

    # Get the parameters
    if modes[2] == "0":
        param1 = memory[memory[ip + 1]]
    else:
        param1 = memory[ip + 1]

    if modes[1] == "0":
        param2 = memory[memory[ip + 2]]
    else:
        param2 = memory[ip + 2]

    if modes[0] == "0":
        memory[memory[ip + 3]] = int(param1 < param2)
    else:
        memory[ip + 3] = int(param1 < param2)

    return ip+4

# Equals
def opcode_08(memory: list, ip: int, modes: str):

    # Get the parameters
    if modes[2] == "0":
        param1 = memory[memory[ip + 1]]
    else:
        param1 = memory[ip + 1]

    if modes[1] == "0":
        param2 = memory[memory[ip + 2]]
    else:
        param2 = memory[ip + 2]

    if modes[0] == "0":
        memory[memory[ip + 3]] = int(param1 == param2)
    else:
        memory[ip + 3] = int(param1 == param2)

    return ip+4

# Table of opcode functions
opcode_functions = [
    opcode_00,
    opcode_01,
    opcode_02,
    opcode_03,
    opcode_04,
    opcode_05,
    opcode_06,
    opcode_07,
    opcode_08,
]


# The IntCode computer
def intcode(memory: List):

    # Setup the computer
    ip = 0

    # Run the program
    while ip < len(memory) and memory[ip] != 99:
        # Encode the opcode
        opcode = f"{memory[ip]:05}"

        # Get the instruction
        instruction = int(opcode[3:])

        # Process the opcode
        ip = opcode_functions[instruction](memory, ip, opcode[0:3])

    print("HALT")


if __name__ == "__main__":

    # Read input
    with open("day05/input.txt") as f:
        memory = [int(x) for x in f.readline().split(",")]

    intcode(memory)
