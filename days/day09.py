from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    res = 0
    for line in data:
        nums = [int(x) for x in line.split()]
        diffs = [nums, *find_diffs(nums)]
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])
        res += diffs[0][-1]
    return res


def find_diffs(row):
    cur = [row[i] - row[i - 1] for i in range(1, len(row))]
    if any(cur):
        return [cur, *find_diffs(cur)]
    else:
        return [cur]


def part_two(data):
    res = 0
    for line in data:
        nums = [int(x) for x in line.split()]
        diffs = [nums, *find_diffs(nums)]

        # Change 1: reverse all lists to avoid prepending
        for i in range(len(diffs)):
            diffs[i] = diffs[i][::-1]

        for i in range(len(diffs) - 2, -1, -1):
            # Change 2: subtract instead of add the differences
            diffs[i].append(diffs[i][-1] - diffs[i + 1][-1])
        res += diffs[0][-1]
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
