from math import ceil

reactions = {}


def get_element(element):
    global reactions

    for k in reactions.keys():
        if k[0] == element:
            return k


def produce(element, quantity, available):
    global reactions

    # Can't produce ore
    if element == "ORE":
        return False

    new_element_key = get_element(element)
    reaction_count = ceil(quantity / new_element_key[1])

    for k, v in reactions[new_element_key].items():
        if not consume(k, v * reaction_count, available):
            return False

    if element not in available:
        available[element] = 0
    available[element] += reaction_count * new_element_key[1]
    return True


def consume(element, quantity, available):
    if quantity <= 0:
        print("Quantity error")
        exit(1)

    if element not in available:
        available[element] = 0

    if available[element] < quantity and not produce(
        element, quantity - available[element], available
    ):
        return False

    available[element] -= quantity
    return True


def part1():
    available = {}
    max_ore = 1_000_000_000_000
    available["ORE"] = max_ore

    consume("FUEL", 1, available)

    return max_ore - available["ORE"]


def part2():
    available = {}
    max_ore = 1_000_000_000_000
    available["ORE"] = max_ore

    produce("FUEL", 1, available)

    ore_consumed = max_ore - available["ORE"]

    while produce("FUEL", max(1, available["ORE"] // ore_consumed), available):
        pass

    return available["FUEL"]


if __name__ == "__main__":

    # Setup the reactions dictionary
    # reactions = {}
    # global reactions

    # Read input
    with open("day14/input.txt") as f:
        for line in f.readlines():
            elements, result = line.strip().split("=>")

            # Add the result
            res_count, res_element = result.strip().split(" ")
            res_count = int(res_count)
            reactions[(res_element.strip(), res_count)] = {}

            # Now we can process the building blocks

            for input_element in elements.strip().split(","):
                elem_count, element = input_element.strip().split(" ")
                elem_count = int(elem_count)
                reactions[(res_element.strip(), res_count)][
                    element
                ] = elem_count

    print(f"Ore: {part1()}")

    print(f"Max Fuel: {part2()}")
