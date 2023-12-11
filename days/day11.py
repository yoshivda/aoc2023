from itertools import combinations

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(abs(x1 - x2) + abs(y1 - y2) +
               sum(min(x1, x2) < col < max(x1, x2)
                   for col in cols)
               + sum(min(y1, y2) < row < max(y1, y2)
                     for row in rows)
               for ((x1, y1), (x2, y2)) in
               combinations({(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '#'}, 2)
               ) \
        if ((cols := [i for i in range(len(data[0])) if all(data[j][i] == '.' for j in range(len(data)))])
            and (rows := [i for i, row in enumerate(data) if all(c == '.' for c in row)])) else 0


def part_two(data):
    return sum(abs(x1 - x2) + abs(y1 - y2) + (
            sum(min(x1, x2) < col < max(x1, x2)
                for col in cols)
            + sum(min(y1, y2) < row < max(y1, y2)
                  for row in rows)
    ) * 999999
               for ((x1, y1), (x2, y2)) in
               combinations({(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '#'}, 2)
               ) \
        if ((cols := [i for i in range(len(data[0])) if all(data[j][i] == '.' for j in range(len(data)))])
            and (rows := [i for i, row in enumerate(data) if all(c == '.' for c in row)])) else 0


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
