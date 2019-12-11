from intcode import IntCode
from collections import defaultdict

if __name__ == "__main__":

    # Read input
    memory = []
    with open("day11/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    robot = IntCode(memory, 0)

    # We start at (0,0) facing up
    x, y = 0, 0
    direction = 1  # left=0, up=1, right=2, down=3
    hull = defaultdict(int)

    xmove = [-1, 0, 1, 0]
    ymove = [0, -1, 0, 1]

    # Part 2
    hull[(0, 0)] = 1
    xmin, xmax, ymin, ymax = 0, 0, 0, 0

    # Run and get two pieces of output
    while not robot.is_halted():
        # Provide our current color
        robot.write_input(hull[x, y])

        # Run until we get the new color output
        robot.run()
        if robot.is_halted():
            break
        color = int(robot.read_output())

        # Run again until we get the new direction
        robot.run()
        turn = (int(robot.read_output()) * 2) - 1

        # Paint the hull
        hull[(x, y)] = color

        # Turn
        direction = (direction + turn) % 4

        # Move
        x += xmove[direction]
        y += ymove[direction]

        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)

        # Get current hull color
        # robot.write_input(hull[x, y])

    print(f"Part 1: Painted = {len(hull.keys())}")

    hull_painted = [[" "] * (xmax - xmin + 1) for _ in range(ymax - ymin + 1)]
    for k in hull.keys():
        x, y = k
        if hull[k] == 1:
            hull_painted[y][x] = "*"

    for i in range(len(hull_painted)):
        print(f"{''.join(hull_painted[i])}")
