import re

from lib import load_input


def solve(data):
    # return part_one(data)
    return part_two(data)


def part_one(data):
    return sum(int((nums := re.findall(r'\d', line))[0] + nums[-1]) for line in data.splitlines())


def part_two(data):
    return sum(int(''.join(
        str(digits[i]) if digits[i].isdigit() else str(nums.index(digits[i]) + 1)
        for i in (0, -1)))
               for line in data.splitlines() if (digits := re.findall(r'(?=(\d|' + '|'.join(
                 (nums := ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])) + '))', line)))


if __name__ == '__main__':
    print(solve(load_input('small2')))
    print(solve(load_input()))
