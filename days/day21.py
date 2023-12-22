from math import floor

from lib import load_input
import numpy as np


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def part_one(data):
    reached = dict()
    todo = {next((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'S')}
    for i in range(7 if len(data) < 20 else 65):  # no example with 64 steps :(
        reached |= {coords: i for coords in todo}
        todo = {(x + dx, y + dy) for dx, dy in directions for x, y in todo
                if 0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data) and data[y + dy][x + dx] != '#'
                and (x + dx, y + dy) not in reached}
    return sum(v % 2 == 0 for v in reached.values())


def part_two(data):
    reached = dict()
    todo = {next((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'S')}
    xs = []
    ys = []
    for i in range(65 + 131 * 3):
        reached |= {coords: i for coords in todo}
        todo = {(x + dx, y + dy) for dx, dy in directions for x, y in todo
                if data[(y + dy) % len(data)][(x + dx) % len(data[0])] != '#'
                and (x + dx, y + dy) not in reached}
        if i % 131 == 65:
            xs.append(i // 131)
            ys.append(sum(v % 2 == i % 2 for v in reached.values()))
    return round(np.polyval(np.polyfit(xs, ys, 2), 202300))


if __name__ == '__main__':
    # print(solve(load_input('small')))
    print(solve(load_input()))
