import math

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(math.floor(math.pow(2, len({int(x) for x in line.split(':')[1].split('|')[0].split()} & {int(x) for x in line.split('|')[1].split()}) - 1)) for line in data)


def part_two(data):
    num_cards = {i: 1 for i in range(1, len(data) + 1)}
    matches = [len({int(x) for x in line.split(':')[1].split('|')[0].split()}
                   & {int(x) for x in line.split('|')[1].split()}) for line in data]
    for i, num in enumerate(matches):
        for j in range(i + 2, i + num + 2):
            num_cards[j] += num_cards[i + 1]
    return sum(num_cards.values())


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
