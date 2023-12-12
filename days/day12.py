import re
from functools import cache

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(num_patterns(re.sub(r'\.+', '.', line.split()[0]) + '.',
                            0, tuple(int(x) for x in line.split()[1].split(',')), 0) for line in data)


@cache
def num_patterns(text, i, nums, j):
    if j == len(nums) and '#' not in text[i:]:
        return 1
    if (i >= len(text) and j < len(nums)) or (j == len(nums) and '#' in text[i:]):
        return 0
    if text[i] == '.':
        return num_patterns(text, i + 1, nums, j)

    return sum(num_patterns(text, x + nums[j] + 1, nums, j + 1)
               for x in range(i, (i + text[i:].index('#') + 1 if '#' in text[i:] else (len(text) - nums[j])))
               if '.' not in text[x:x + nums[j]] and text[x + nums[j]] != '#')


def part_two(data):
    return sum(num_patterns('?'.join([re.sub(r'\.+', '.', line.split()[0])] * 5) + '.', 0,
                            tuple(int(x) for x in line.split()[1].split(',')) * 5, 0) for line in data)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
