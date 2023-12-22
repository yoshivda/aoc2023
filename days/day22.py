import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    bricks = [(*(eval(x) for x in line.split('~')), i) for i, line in enumerate(data)]
    grid = dict()
    for ((x1, y1, z1), (x2, y2, z2), i) in sorted(bricks, key=lambda t: min(t[0][2], t[1][2])):
        while all((x, y, z - 1) not in grid and min(z1, z2) > 1
                  for x in range(min(x1, x2), max(x1, x2) + 1)
                  for y in range(min(y1, y2), max(y1, y2) + 1)
                  for z in range(min(z1, z2), max(z1, z2) + 1)):
            z1 -= 1
            z2 -= 1
        grid |= {(x, y, z): i
                 for x in range(min(x1, x2), max(x1, x2) + 1)
                 for y in range(min(y1, y2), max(y1, y2) + 1)
                 for z in range(min(z1, z2), max(z1, z2) + 1)}
    supported_by = {i: {grid[x, y, z - 1] for x, y, z in {k for k, v in grid.items() if v == i}
                        if (x, y, z - 1) in grid and grid[x, y, z - 1] != i} for i in range(len(bricks))}
    supports = {i: {grid[x, y, z + 1] for x, y, z in {k for k, v in grid.items() if v == i}
                    if (x, y, z + 1) in grid and grid[x, y, z + 1] != i} for i in range(len(bricks))}
    return sum(all(len(supported_by[b]) > 1 for b in supports[i]) for i in range(len(bricks)))


def part_two(data):
    bricks = sorted([(*(eval(x) for x in line.split('~')), i) for i, line in enumerate(data)], key=lambda t: min(t[0][2], t[1][2]))
    grid = dict()
    for ((x1, y1, z1), (x2, y2, z2), i) in bricks:
        while all((x, y, z - 1) not in grid and min(z1, z2) > 1
                  for x in range(min(x1, x2), max(x1, x2) + 1)
                  for y in range(min(y1, y2), max(y1, y2) + 1)
                  for z in range(min(z1, z2), max(z1, z2) + 1)):
            z1 -= 1
            z2 -= 1
        grid |= {(x, y, z): i
                 for x in range(min(x1, x2), max(x1, x2) + 1)
                 for y in range(min(y1, y2), max(y1, y2) + 1)
                 for z in range(min(z1, z2), max(z1, z2) + 1)}
    supported_by = {i: {grid[x, y, z - 1] for x, y, z in {k for k, v in grid.items() if v == i}
                        if (x, y, z - 1) in grid and grid[x, y, z - 1] != i} for i in range(len(bricks))}
    res = 0
    for idx, (_, _, i) in enumerate(bricks):
        falling = {i}
        for b in bricks[idx:]:
            if supported_by[b[2]] and supported_by[b[2]] <= falling:
                falling.add(b[2])
        res += len(falling) - 1
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
