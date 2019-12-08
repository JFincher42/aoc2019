from collections import defaultdict

if __name__ == "__main__":

    w, t = 25, 6
    blocksize = w * t
    start = 0

    # Read input
    with open("day08/input.txt") as f:
        input_string = f.readline().strip()

    layers = []
    while start < len(input_string):
        new_layer = defaultdict(int)
        for pixel in input_string[start : start + blocksize]:
            new_layer[pixel] += 1
        start += blocksize
        layers.append(new_layer)

    lowest = layers[0]
    for layer in layers:
        if layer["0"] < lowest["0"]:
            lowest = layer

    print(f"Part 1: Lowest = {lowest['1'] * lowest['2']}")

    final = [" "] * blocksize
    max_layer = len(input_string) // blocksize

    for index in range(blocksize):
        current_layer = 0
        while (
            current_layer < max_layer
            and input_string[current_layer * blocksize + index] == "2"
        ):
            current_layer += 1
        if input_string[current_layer * blocksize + index] == '1':
            final[index] = "*"

    print("Part 2: ")
    for width in range(0, blocksize, w):
        print(f"  {''.join(final[width:width+w])}")
