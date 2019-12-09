### IntCode computer
from typing import List
from collections import deque


class IntCode:
    def __init__(self, memory: List, ip: int = 0):

        self._memory = memory.copy()
        self._ip = ip
        self._mem_len = len(self._memory)

        # Internal state
        self._paused = False
        self._halted = False

        # Input and output queues
        self._input = deque([])
        self._output = deque([])
        self._last_output = ""

        # Opcode function table
        self._opcode_functions = [
            self._opcode_00,
            self._opcode_01,
            self._opcode_02,
            self._opcode_03,
            self._opcode_04,
            self._opcode_05,
            self._opcode_06,
            self._opcode_07,
            self._opcode_08,
        ]

    def is_halted(self):
        return self._halted

    # Something has gone horribly wrong, just end it all
    def _opcode_00(self, modes: str):
        print("ERROR")
        self._halted = True
        return self._mem_len

    # Add two numbers
    def _opcode_01(self, modes: str):

        # Get the parameters
        if modes[2] == "0":
            param1 = self._memory[self._memory[self._ip + 1]]
        else:
            param1 = self._memory[self._ip + 1]

        if modes[1] == "0":
            param2 = self._memory[self._memory[self._ip + 2]]
        else:
            param2 = self._memory[self._ip + 2]

        # Third parameter is always 0
        self._memory[self._memory[self._ip + 3]] = param1 + param2

        # Where is the next self._IP?
        return self._ip + 4

    # Multiply two numbers
    def _opcode_02(self, modes: str):

        # Get the parameters
        if modes[2] == "0":
            param1 = self._memory[self._memory[self._ip + 1]]
        else:
            param1 = self._memory[self._ip + 1]

        if modes[1] == "0":
            param2 = self._memory[self._memory[self._ip + 2]]
        else:
            param2 = self._memory[self._ip + 2]

        self._memory[self._memory[self._ip + 3]] = param1 * param2

        # Where is the next self._IP?
        return self._ip + 4

    # Get user input
    def _opcode_03(self, modes: str):

        # Get user input
        user_input = int(self._read_input())

        if modes[2] == "0":
            self._memory[self._memory[self._ip + 1]] = user_input
        else:
            self._memory[self._ip + 1] = user_input

        return self._ip + 2

    # Print output
    def _opcode_04(self, modes: str):

        # Get parameters
        if modes[2] == "0":
            self._write_output(f"{self._memory[self._memory[self._ip + 1]]}")
        else:
            self._write_output(f"{self._memory[self._ip + 1]}")

        self._paused = True
        return self._ip + 2

    # Jump if true
    def _opcode_05(self, modes: str):

        # Get the parameters
        if modes[2] == "0":
            param1 = self._memory[self._memory[self._ip + 1]]
        else:
            param1 = self._memory[self._ip + 1]

        if modes[1] == "0":
            param2 = self._memory[self._memory[self._ip + 2]]
        else:
            param2 = self._memory[self._ip + 2]

        if param1 != 0:
            self._ip = param2
        else:
            self._ip += 3

        return self._ip

    # Jump if false
    def _opcode_06(self, modes: str):

        # Get the parameters
        if modes[2] == "0":
            param1 = self._memory[self._memory[self._ip + 1]]
        else:
            param1 = self._memory[self._ip + 1]

        if modes[1] == "0":
            param2 = self._memory[self._memory[self._ip + 2]]
        else:
            param2 = self._memory[self._ip + 2]

        if param1 == 0:
            self._ip = param2
        else:
            self._ip += 3

        return self._ip

    # Less than
    def _opcode_07(self, modes: str):

        # Get the parameters
        if modes[2] == "0":
            param1 = self._memory[self._memory[self._ip + 1]]
        else:
            param1 = self._memory[self._ip + 1]

        if modes[1] == "0":
            param2 = self._memory[self._memory[self._ip + 2]]
        else:
            param2 = self._memory[self._ip + 2]

        if modes[0] == "0":
            self._memory[self._memory[self._ip + 3]] = int(param1 < param2)
        else:
            self._memory[self._ip + 3] = int(param1 < param2)

        return self._ip + 4

    # Equals
    def _opcode_08(self, modes: str):

        # Get the parameters
        if modes[2] == "0":
            param1 = self._memory[self._memory[self._ip + 1]]
        else:
            param1 = self._memory[self._ip + 1]

        if modes[1] == "0":
            param2 = self._memory[self._memory[self._ip + 2]]
        else:
            param2 = self._memory[self._ip + 2]

        if modes[0] == "0":
            self._memory[self._memory[self._ip + 3]] = int(param1 == param2)
        else:
            self._memory[self._ip + 3] = int(param1 == param2)

        return self._ip + 4

    # I/O functions

    def write_input(self, item: str):
        self._input.append(item)

    def _read_input(self):
        return self._input.popleft()

    def _write_output(self, item: str):
        self._output.append(item)

    def read_output(self):
        if len(self._output):
            self._last_output = self._output.popleft()
        return self._last_output

    # The IntCode computer
    def run(self):

        # First check if we're halted

        if self._halted:
            return -1

        # Unpause
        self._paused = False

        # Check if we should be halted
        self._halted = (
            self._ip == -1
            or self._ip >= self._mem_len
            or self._memory[self._ip] == 99
        )

        # Run the program
        while (
            self._ip < self._mem_len and not self._paused and not self._halted
        ):
            # Encode the opcode
            opcode = f"{self._memory[self._ip]:05}"

            # Get the instruction
            instruction = int(opcode[3:])

            # Process the opcode
            if instruction == 99:
                self._halted = True
            else:
                self._ip = self._opcode_functions[instruction](
                    opcode[0:3]
                )

        if self._halted:
            return -1
        else:
            return self._ip
