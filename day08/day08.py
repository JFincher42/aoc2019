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
