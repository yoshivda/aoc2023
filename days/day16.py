from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return trace((-1, 0, 1, 0), data)


def trace(beam, grid):
    beams = [beam]
    seen = set()
    while beams:
        new_beams = []
        for x, y, dx, dy in beams:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)) or (nx, ny, dx, dy) in seen:
                continue
            seen.add((nx, ny, dx, dy))
            match grid[ny][nx]:
                case '.':
                    new_beams.append((nx, ny, dx, dy))
                case '/':
                    new_beams.append((nx, ny, -dy, -dx))
                case '\\':
                    new_beams.append((nx, ny, dy, dx))
                case '|':
                    if dx:
                        new_beams.append((nx, ny, 0, 1))
                        new_beams.append((nx, ny, 0, -1))
                    else:
                        new_beams.append((nx, ny, dx, dy))
                case '-':
                    if dy:
                        new_beams.append((nx, ny, 1, 0))
                        new_beams.append((nx, ny, -1, 0))
                    else:
                        new_beams.append((nx, ny, dx, dy))
        beams = new_beams
    return len({t[:2] for t in seen})


def part_two(data):
    beams = {(x, y, dx, 0) for y in range(len(data)) for x, dx in ((-1, 1), (len(data[0]), -1))} |\
             {(x, y, 0, dy) for x in range(len(data[0])) for y, dy in ((-1, 1), (len(data), -1))}
    return max(trace(beam, data) for beam in beams)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))




