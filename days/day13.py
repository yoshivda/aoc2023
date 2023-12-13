from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def part_one(data):
    return sum(check_grid(grid.splitlines(), 0) for grid in data)


def part_two(data):
    return sum(check_grid(grid.splitlines(), 1) for grid in data)


def col(grid, i):
    return [grid[x][i] for x in range(len(grid))]


def check_grid(grid, req_diffs):
    # horiz mirror
    for i in range(len(grid) - 1):
        if (diffs := sum(grid[i][x] != grid[i + 1][x] for x in range(len(grid[0])))) <= req_diffs:
            for j in range(1, min(i + 1, len(grid) - i - 1)):
                diffs += sum(grid[i - j][x] != grid[i + 1 + j][x] for x in range(len(grid[0])))
                if diffs > req_diffs:
                    break
            else:
                if diffs == req_diffs:
                    return (i + 1) * 100

    # vert mirror
    for i in range(len(grid[0]) - 1):
        if (diffs := sum(col(grid, i)[x] != col(grid, i + 1)[x] for x in range(len(grid)))) <= req_diffs:
            for j in range(1, min(i + 1, len(grid[0]) - i - 1)):
                diffs += sum(col(grid, i - j)[x] != col(grid, i + 1 + j)[x] for x in range(len(grid)))
                if diffs > req_diffs:
                    break
            else:
                if diffs == req_diffs:
                    return i + 1
    raise Exception


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
