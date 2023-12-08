import math
import re

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    inst = data[0]
    route = {match[0]: match[1:] for line in data[2:] if (match := re.findall(r'\w{3}', line))}
    return find_route('AAA', 'ZZZ', inst, route)


def find_route(start, end_suffix, inst, route):
    res = 0
    cur = start
    while not cur.endswith(end_suffix):
        cur = route[cur][int(inst[res % len(inst)] == 'R')]
        res += 1
    return res


def part_two(data):
    inst = data[0]
    route = {match[0]: match[1:] for line in data[2:] if (match := re.findall(r'\w{3}', line))}
    starts = [k for k in route.keys() if k.endswith('A')]
    periods = [find_route(start, 'Z', inst, route) for start in starts]
    return math.lcm(*periods)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('medium')))
    print(solve(load_input()))
