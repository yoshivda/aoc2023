import heapq

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    q = [(0, 0, 0, 1, 0)]
    dists = {(0, 0): 0}
    states = set()
    while q:
        dist, x, y, dir, rep = heapq.heappop(q)
        if (x, y, dir, rep) in states:
            continue
        states.add((x, y, dir, rep))
        if (x, y) == (len(data[0]) - 1, len(data) - 1):
            return dist
        for nx, ny, ndir in around(x, y, dir):
            if not (0 <= nx < len(data[0]) and 0 <= ny < len(data)):
                continue
            if dir == ndir and rep == 3:
                continue
            ndist = dist + int(data[ny][nx])
            if (nx, ny) not in dists or ndist < dists[nx, ny]:
                dists[nx, ny] = ndist
            nrep = rep + 1 if dir == ndir else 1
            state = nx, ny, ndir, nrep
            if state not in states:
                heapq.heappush(q, (ndist, nx, ny, ndir, nrep))


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def around(x, y, direction):
    return [(x + ndx, y + ndy, dir) for dir, (ndx, ndy) in enumerate(directions) if (dir + 2) % 4 != direction]


def part_two(data):
    q = [(0, 0, 0, 1, 0)]
    dists = {(0, 0): 0}
    states = set()
    while q:
        dist, x, y, dir, rep = heapq.heappop(q)
        if (x, y, dir, rep) in states:
            continue
        states.add((x, y, dir, rep))
        if (x, y) == (len(data[0]) - 1, len(data) - 1) and rep >= 4:
            return dist
        for nx, ny, ndir in around(x, y, dir):
            if not (0 <= nx < len(data[0]) and 0 <= ny < len(data)):
                continue
            if dir != ndir and 0 < rep < 4:
                continue
            if dir == ndir and rep == 10:
                continue
            ndist = dist + int(data[ny][nx])
            if (nx, ny) not in dists or ndist < dists[nx, ny]:
                dists[nx, ny] = ndist
            nrep = rep + 1 if dir == ndir else 1
            state = nx, ny, ndir, nrep
            if state not in states:
                heapq.heappush(q, (ndist, nx, ny, ndir, nrep))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('pt2')))
    print(solve(load_input()))
