import math

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return math.prod(sum((time - i) * i > dist for i in range(time))
                     for time, dist in zip(*([int(x) for x in line.split()[1:]] for line in data)))


def part_two(data):
    return sum((t[0] - i) * i > t[1] for i in range(t[0]))\
        if (t := [int(''.join(line.split()[1:])) for line in data]) else 0


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
