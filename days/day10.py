from lib import load_input

tiles = {'|': ((0, -1), (0, 1)),
         '-': ((-1, 0), (1, 0)),
         'L': ((0, -1), (1, 0)),
         'J': ((0, -1), (-1, 0)),
         '7': ((0, 1), (-1, 0)),
         'F': ((0, 1), (1, 0)),
         }


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    grid = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line) if c == 'S' or c in tiles.keys()}
    x, y = next(k for k, v in grid.items() if v == 'S')
    for pos in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if pos in grid and (path := follow_path(pos, (x, y), grid)):
            # print(path)
            return len(path) // 2 + 1


def follow_path(pos, prev, grid):
    res = [pos]
    seen = {pos}
    while True:
        for delta in tiles[grid[pos]]:
            new_pos = pos[0] + delta[0], pos[1] + delta[1]
            if new_pos == prev:
                continue
            if new_pos not in grid or new_pos in seen:
                return []
            if grid[new_pos] == 'S':
                return res
            res.append(new_pos)
            seen.add(new_pos)
            prev = pos
            pos = new_pos
            break


def part_two(data):
    grid = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line) if c == 'S' or c in tiles.keys()}
    x, y = next(k for k, v in grid.items() if v == 'S')
    for pos in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if pos in grid and (path := follow_path(pos, (x, y), grid)):
            break
    path.append((x, y))
    path = set(path)
    res = 0
    for y in range(len(data)):
        inside = False
        for x in range(len(data[0])):
            if (x, y) in path:
                if grid[x, y] in '|JL':
                    inside = not inside
            elif inside:
                res += 1
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('medium')))
    print(solve(load_input('large')))
    print(solve(load_input()))
