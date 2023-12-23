import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def part_one(data):
    startx = data[0].index('.')
    endx = data[-1].index('.')
    todo = [(startx, 0, {(startx, 0)})]
    res = 0
    while todo:
        x, y, seen = todo.pop()
        if y == len(data) - 1 and x == endx:
            res = max(res, len(seen) - 1)
        if data[y][x] == '.':
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] != '#' and (nx, ny) not in seen:
                    todo.append((nx, ny, seen | {(nx, ny)}))
        elif data[y][x] in 'v^<>':
            dx, dy = directions['>v<^'.index(data[y][x])]
            if (x + dx, y + dy) not in seen:
                todo.append((x + dx, y + dy, seen | {(x + dx, y + dy)}))
    return res


def part_two(data):
    startx = data[0].index('.')
    endx = data[-1].index('.')
    nodes = dict()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                continue
            nodes[x, y] = {(x + dx, y + dy): 1 for dx, dy in directions if 0 <= x + dx < len(data[0])
                           and 0 <= y + dy < len(data) and data[y + dy][x + dx] != '#'}
    for node, neighs in nodes.items():
        if len(neighs) != 2:
            continue
        dist = sum(neighs.values())
        nlist = list(neighs)
        for i in range(2):
            del nodes[nlist[i]][node]
            nodes[nlist[i]][nlist[(i + 1) % 2]] = dist

    todo = [(startx, 0, {(startx, 0)}, 0)]
    res = 0
    while todo:
        x, y, seen, dist = todo.pop()
        if y == len(data) - 1 and x == endx:
            res = max(res, dist)
        for (nx, ny), ndist in nodes[x, y].items():
            if (nx, ny) not in seen:
                todo.append((nx, ny, seen | {(nx, ny)}, dist + ndist))
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
