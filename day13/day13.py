from intcode import IntCode
from collections import defaultdict
from os import system


def update_game_data(game_field, x, y, val):

    if val == 1:
        game_field[y][x] = "X"
    elif val == 2:
        game_field[y][x] = "%"
    elif val == 3:
        game_field[y][x] = "_"
    elif val == 4:
        game_field[y][x] = "o"
    else:
        game_field[y][x] = " "


if __name__ == "__main__":

    # Read input
    memory = []
    with open("day13/input.txt") as f:
        for line in f.readlines():
            memory.extend([int(x) for x in line.split(",")])

    # Create new IntCode instance
    intcode = IntCode(memory, 0)
    # Part 1

    game_data = defaultdict(int)

    # intcode.run()
    # while not intcode.is_halted():
    #     x_pos = int(intcode.read_output())
    #     intcode.run()
    #     y_pos = int(intcode.read_output())
    #     intcode.run()
    #     tile_id = int(intcode.read_output())
    #     intcode.run()

    #     game_data[(x_pos, y_pos)] = tile_id

    # tile_count = [0] * 5
    # for id in game_data.values():
    #     tile_count[id] += 1

    # print(f"Part 1: Count of '2's = {tile_count[2]}")

    # # Part 2
    memory[0] = 2
    # intcode.reset()
    game_field = [[" " for _ in range(38)] for _ in range(38)]
    intcode.run()
    while not intcode.is_halted():
        x_pos = int(intcode.read_output())
        intcode.run()
        y_pos = int(intcode.read_output())
        intcode.run()
        tile_id = int(intcode.read_output())
        intcode.run()

        # update_game_data(game_data, x_pos, y_pos, tile_id)
        # draw_game_field(game_data, game_field)
        if (x_pos, y_pos) == (-1, 0):
            print(f"Score: {tile_id}")
        else:
            update_game_data(game_field, x_pos, y_pos, tile_id)
            for y in range(38):
                print(f"{''.join(game_field[y])}")
            input()
