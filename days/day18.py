from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def part_one(data):
    dug = {(0, 0)}
    x, y = 0, 0
    for line in data:
        dir, num, _ = line.split()
        dx, dy = directions['RDLU'.index(dir)]
        for _ in range(int(num)):
            x += dx
            y += dy
            dug.add((x, y))
    todo = [(1, 1)]
    seen = set()
    while todo:
        x, y = todo.pop()
        for dx, dy in directions:
            new = x + dx, y + dy
            if new in seen:
                continue
            if ((x, y) in dug and new in dug) or (x, y) not in dug:
                seen.add(new)
                todo.append(new)
    return len(seen)


def part_two(data):
    points = [(0, 0)]
    x, y = 0, 0
    perim = 0
    for line in data:
        thing = line.split()[2][2:-1]
        num = int(thing[:5], 16)
        dx, dy = directions[int(thing[-1])]
        x += num * dx
        y += num * dy
        points.append((x, y))
        perim += num
    return (abs(sum((points[i][0] + points[i + 1][0]) * (points[i + 1][1] - points[i][1])
                    for i in range(len(points) - 1)))
            + perim) // 2 + 1


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
