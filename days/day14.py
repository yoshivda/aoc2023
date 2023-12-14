from collections import defaultdict, Counter

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    grid = [list(row) for row in data]
    # rotate 90 ccw, north is now left
    grid = [col(grid, -1 - i) for i in range(len(grid))]
    # move left
    grid = [move_to_start(grid[i]) for i in range(len(grid))]
    # rotate 90 cw, north is back north
    grid = [col(grid, i)[::-1] for i in range(len(grid[0]))]
    return sum(Counter(row)['O'] * (len(data) - i) for i, row in enumerate(grid))


def move_to_start(row):
    res = ['.'] * len(row)
    next_pos = 0
    for j, c in enumerate(row):
        if c == '#':
            res[j] = '#'
            next_pos = j + 1
        elif c == 'O':
            res[next_pos] = 'O'
            next_pos += 1
    return res


def part_two(data):
    grid = [list(row) for row in data]
    states = dict()
    i = 0
    while i < 1000000000:
        grid = cycle(grid)
        txt = '\n'.join(''.join(row) for row in grid)
        if txt in states and states[txt]:
            step = i - states[txt]
            i += ((1000000000 - i) // step) * step
        states[txt] = i
        i += 1
    return sum(Counter(row)['O'] * (len(data) - i) for i, row in enumerate(grid))


def col(grid, i):
    return [grid[x][i] for x in range(len(grid))]


def cycle(grid):
    # rotate 90 ccw, north is now left
    grid = [col(grid, -1 - i) for i in range(len(grid))]
    for _ in range(4):
        # move west
        grid = [move_to_start(grid[i]) for i in range(len(grid))]
        # rotate 90 cw
        grid = [col(grid, i)[::-1] for i in range(len(grid[0]))]

    # rotate back 90 cw, north faces top
    grid = [col(grid, i)[::-1] for i in range(len(grid[0]))]
    return grid


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
