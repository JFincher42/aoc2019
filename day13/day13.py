from intcode import IntCode
from collections import defaultdict

if __name__ == "__main__":

    # Read input
    memory = []
    with open("day13/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    # Create new IntCode instance
    intcode = IntCode(memory, 0)
    # Part 1

    game_field = defaultdict(int)

    intcode.run()
    while not intcode.is_halted():
        x_pos = int(intcode.read_output())
        intcode.run()
        y_pos = int(intcode.read_output())
        intcode.run()
        tile_id = int(intcode.read_output())
        intcode.run()

        game_field[(x_pos, y_pos)] = tile_id

    tile_count = [0] * 5
    for id in game_field.values():
        tile_count[id] += 1

    print(f"Part 1: Count of '2's = {tile_count[2]}")
