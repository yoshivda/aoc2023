import re
import string
import time
from itertools import combinations

from sympy import Point, Polygon, Segment, Ray, solve as sympysolve, symbols, Eq

from lib import load_input


def solve(data):
    return part_one(data.splitlines())
    # return part_two(data.splitlines())


def part_one(data):
    points = [tuple(int(x) for x in re.findall(r'-?\d+', line)) for line in data]
    lo, hi = (7, 27) if len(data) == 5 else (200000000000000, 400000000000000)
    box = Polygon(Point(lo, lo), Point(lo, hi), Point(hi, hi), Point(hi, lo))
    lines = []
    for x, y, _, vx, vy, _ in points:
        ray = Ray(Point(x, y), Point(x + vx, y + vy))
        ints = box.intersection(ray)
        if len(ints) == 1:
            ints.append(ray.source)
        elif len(ints) == 0:
            continue
        lines.append(Segment(*[Point(*p) for p in ints]))
    return sum(bool(l1.intersection(l2)) for l1, l2 in combinations(lines, 2))


def part_two(data):
    return (lambda syms: sum(sympysolve([Eq(tup[d] + syms[6 + i] * tup[3 + d], syms[d] + syms[6 + i] * syms[3 + d])
                                         for d in range(3) for i, tup in enumerate(
            [tuple(int(x) for x in re.findall(r'-?\d+', line)) for line in data[:5]])], syms)[0][:3]))(
        symbols(' '.join(list(string.ascii_letters[:11]))))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
