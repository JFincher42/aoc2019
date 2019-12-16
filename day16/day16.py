base_pattern = [0, 1, 0, -1]


def get_pattern(position):
    pattern = []
    current_base = 0
    for _ in range(0, signal_length + 1, position):
        pattern.extend([base_pattern[current_base]] * position)
        current_base = (current_base + 1) % 4
    remaining = signal_length - len(pattern) + 1
    pattern.extend([base_pattern[current_base]] * remaining)
    return pattern[1:]


def apply_pattern(signal, pattern):
    return [x[0] * x[1] for x in zip(signal, pattern)]


if __name__ == "__main__":
    global signal_length

    # Read input
    with open("day16/input.txt") as f:
        signal = [int(x) for x in list(f.readline().strip())]

    signal_length = len(signal)

    for phase in range(100):
        output_signal = []
        for position in range(signal_length):
            pattern = get_pattern(position + 1)
            output = apply_pattern(signal, pattern)
            output_signal.append(abs(sum(output)) % 10)
        signal = output_signal.copy()

    print(f"Output signal: {output_signal[:8]}")
