from math import ceil
from collections import defaultdict

# base_pattern = [0, 1, 0, -1]
patterns = defaultdict(list)


def get_coeffs(signal_length, phases):
    coeffs = [0] * signal_length
    coeffs[0] = 1
    x = 1
    for n in range(2, signal_length + 1):
        x *= n + phases - 1
        x //= n - 1
        coeffs[n - 1] = x % 10
    return coeffs


def get_pattern(position):
    global patterns

    if position in patterns.keys():
        return patterns[position]

    repeats = ceil(signal_length / (position * 4))
    base0 = [0] * position
    base1 = [1] * position
    base2 = [-1] * position

    pattern = base0.copy() + base1.copy() + base0.copy() + base2.copy()
    pattern *= repeats

    patterns[position] = pattern[1 : signal_length + 1]
    return pattern[1 : signal_length + 1]


def apply_pattern(signal, pattern, position):
    return [x[0] * x[1] for x in zip(signal[position:], pattern[position:])]


if __name__ == "__main__":
    global signal_length

    # Read input
    with open("day16/input.txt") as f:
        signal = [int(x) for x in list(f.readline().strip())]

    signal = signal * 10_000
    signal_length = len(signal)
    offset = int("".join([str(x) for x in signal[:7]]))

    coeffs = get_coeffs(signal_length, 99)
    output_signal = [0] * 8
    for i in range(8):
        output_signal[i] = sum(
            [(x * y) % 10 for x, y in zip(signal[offset + i :], coeffs)]
        ) % 10
    print(f"Signal length = {signal_length}")
    # for phase in range(100):
    #     print(f"Phase {phase}...")
    #     output_signal = []
    #     for position in range(signal_length):
    #         pattern = get_pattern(position + 1)
    #         output = apply_pattern(signal, pattern, position)
    #         output_signal.append(abs(sum(output)) % 10)
    #     signal = output_signal.copy()

    # print(f"Output signal: {output_signal[:8]}")
    print(f"Output signal: {output_signal}")
