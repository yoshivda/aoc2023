import math
import re

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    res = 0
    for line in data:
        game_id = re.search(r'\d+', line).group()
        draws = line.split(':')[1].replace(';', ',').split(',')
        for info in draws:
            number, colour = info.split()
            if (colour == 'red' and int(number) > 12) \
                    or (colour == 'green' and int(number) > 13) \
                    or (colour == 'blue' and int(number) > 14):
                break
        else:
            res += int(game_id)
    return res


def part_two(data):
    res = 0
    for line in data:
        draws = line.split(':')[1].replace(';', ',').split(',')
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for info in draws:
            number, colour = info.split()
            min_cubes[colour] = max(min_cubes[colour], int(number))
        res += math.prod(min_cubes.values())
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
