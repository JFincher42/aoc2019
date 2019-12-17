from intcode import IntCode

if __name__ == "__main__":
    global intcode

    # Read input
    memory = []
    with open("day17/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    intcode = IntCode(memory, 0)
    scaffold = []
    scaffold_line = []

    intcode.run()
    while not intcode.is_halted():
        char = int(intcode.read_output())
        if char == 10:
            scaffold.append(scaffold_line.copy())
            scaffold_line.clear()
        else:
            scaffold_line.extend(chr(char))
        intcode.run()

    intersections = 0
    for y in range(1, len(scaffold) - 2):
        scaffold_line = scaffold[y]
        for x in range(len(scaffold_line) - 1):
            if "".join(scaffold_line[x : x + 3]) == ".#.":
                scaffold_line_2 = scaffold[y + 1]
                if "".join(scaffold_line_2[x : x + 3]) == "###":
                    scaffold_line_3 = scaffold[y + 2]
                    if "".join(scaffold_line_3[x : x + 3]) == ".#.":
                        intersections += (x + 1) * (y + 1)

    for line in scaffold:
        print(f"{''.join(line)}")
    print(f"\nIntersections: {intersections}")
