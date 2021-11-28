from pprint import pprint
import pathlib

root_path = pathlib.Path.home() / "git" / "aoc2019" / "day22"


def part1(lines, cards):
    for line in lines:
        if line == "deal into new stack":
            cards.reverse()
        elif line.startswith("deal with increment "):
            skip = int(line.removeprefix("deal with increment "))
            new_cards = cards.copy()
            count, current = 0, 0
            while count < len(cards):
                new_cards[current] = cards[count]
                current = (current + skip) % len(cards)
                count += 1
            cards = new_cards
        else:
            count = int(line.removeprefix("cut "))
            cards = cards[count:] + cards[:count]

    # return cards
    return cards.index(2019)


def part2(lines):

    return -1


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # cards = [x for x in range(10)]
    cards = [x for x in range(10007)]

    pprint(f"Part 1: Answer: {part1(lines, cards)}")

    cards = [x for x in range(119315717514047)]
    print(f"Part 2: Answer: {part1(lines, cards)}")
