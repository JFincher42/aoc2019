from intcode import IntCode


if __name__ == "__main__":
    global intcode

    # Read input
    memory = []
    with open("day21/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    # Part 1
    # spring_prog = "OR A J\nAND B J\nAND C J\nNOT J J\nAND D J\nWALK\n"
    # Part 2
    spring_prog = "NOT H J\nOR C J\nAND B J\nAND A J\nNOT J J\nAND D J\nRUN\n"
    output_chars = []

    springbot = IntCode(memory, 0)
    for ch in spring_prog:
        springbot.write_input(str(ord(ch)))

    springbot.run()
    output = int(springbot.read_output())
    
    while not springbot.is_halted() and output < 256:
        output_chars.append(chr(output))
        springbot.run()
        if not springbot.is_halted():
            output = int(springbot.read_output())

    if output > 255:
        print(f"Damage: {output}")
    else:
        print(f"Hull: {''.join(output_chars)}")
