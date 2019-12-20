from intcode import IntCode


def get_tractor_pull(x, y):
    global memory

    drone = IntCode(memory, 0)
    drone.write_input(x)
    drone.write_input(y)
    drone.run()
    return int(drone.read_output())


def find_tractor_width(x, y):

    x_start, x_end = 0, 0
    x = 0
    found_start, found_end = False, False
    while not found_end:
        tractor_pull = get_tractor_pull(x, y)

        # If we haven't yet found the start
        if not found_start:
            # Keep going until we do
            if tractor_pull:
                found_start = True
                x_start = x

        # After we've found the start, stop when it ends
        else:
            if not tractor_pull:
                found_end = True
                x_end = x - 1

        x += 1

    return x_start, x_end


if __name__ == "__main__":
    global memory

    # Read input
    memory = []
    with open("day19/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.strip().split(",")])

    points = 0

    # for y in range(50):
    #     found_start = False
    #     for x in range(50):
    #         tractor_pull = get_tractor_pull(x, y)

    #         # If we haven't yet found the start
    #         if not found_start:
    #             # Keep going until we do
    #             if tractor_pull:
    #                 found_start = True
    #                 points += 1

    #         # After we've found the start, stop when it ends
    #         else:
    #             if tractor_pull:
    #                 points += 1
    #             else:
    #                 break

    print(f"Points: {points}")

    width = 100
    y = 2
    x_start, x_end = find_tractor_width(0, y)
    print(f"Row {y}, width = {x_end - x_start}")
    while x_end - x_start + 1 < width:
        y += 1
        x_start, x_end = find_tractor_width(x_start, y)
        # print(f"Row {y}, width = {x_end - x_start}")

    y_start = y
    print(
        f"Found first row at y={y_start}, tractor at {x_start} through {x_end}"
    )

    bottom_left = get_tractor_pull(x_end - width + 1, y_start + width - 1)
    bottom_right = get_tractor_pull(x_end, y_start + width - 1)

    while not (bottom_left and bottom_right):
        y_start += 1
        x_start, x_end = find_tractor_width(x_start, y_start)
        bottom_left = get_tractor_pull(x_end - width + 1, y_start + width - 1)
        bottom_right = get_tractor_pull(x_end, y_start + width - 1)

    print(f"Found ({x_end-width+1}, {y_start}), answer = {(x_end-width+1) * 10_000 + y_start}")