import math
import re

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(int(match.group()) for y, line in enumerate(data) for match in re.finditer(r'\d+', line) if
               any(data[y + dy][x + dx] != '.' and not data[y + dy][x + dx].isnumeric()
                   for x in range(*match.span()) for dx in range(-1, 2) for dy in range(-1, 2)
                   if (dx or dy) and (0 <= x + dx < len(data[0])
                                      and 0 <= y + dy < len(data))))


def part_two(data):
    return sum(math.prod(parts_around) for x, y in
               [(x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == '*']  # Potential gears
               if len(parts_around :=
                      # Find part number coordinates around gear position
                      {coords[(x + dx, y + dy)] for dx in range(-1, 2) for dy in range(-1, 2)
                       if (dx or dy) and (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data))
                       and (x + dx, y + dy) in
                       # Find all part numbers' coordinates
                       (coords := {(x, y): num for (num, x1, x2, y) in
                        [(num, x1, x2, y) for(num, x1, x2, y) in
                         # Find all number positions
                         [(int(match.group()), *match.span(), y) for y, line in enumerate(data)
                          for match in re.finditer(r'\d+', line)]
                         # Check if surrounded by a symbol
                         if any(data[y + dy][x + dx] != '.' and not data[y + dy][x + dx].isnumeric()
                                for x in range(x1, x2) for dx in range(-1, 2) for dy in range(-1, 2)
                                if (dx or dy) and (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data)))]
                        for x in range(x1, x2)})}) == 2)


if __name__ == '__main__':
    print(solve(load_input('small')))
    # print(solve(load_input('small2')))
    print(solve(load_input()))
