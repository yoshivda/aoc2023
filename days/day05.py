from lib import load_input


def solve(data):
    # return part_one(data)
    return part_two(data)


def part_one(data):
    seeds = [int(x) for x in data.split('\n\n')[0].split()[1:]]
    for part in data.split('\n\n')[1:]:
        replaced = [False for _ in seeds]
        for line in part.splitlines()[1:]:
            dest_start, src_start, range_size = (int(x) for x in line.split())
            for i, seed in enumerate(seeds):
                if not replaced[i] and 0 <= seed - src_start < range_size:
                    seeds[i] = dest_start + (seed - src_start)
                    replaced[i] = True
    return min(seeds)


def part_two(data):
    nums = data.split('\n\n')[0].split()[1:]
    ranges = [(int(nums[i]), int(nums[i]) + int(nums[i + 1])) for i in range(0, len(nums), 2)]
    for part in data.split('\n\n')[1:]:
        result = []
        new_ranges = []
        for line in part.splitlines()[1:]:
            dest_start, src_start, range_size = (int(x) for x in line.split())
            new_ranges = []
            for start, end in ranges:
                overlap_start, overlap_end = max(start, src_start), min(end, src_start + range_size)
                if overlap_start >= overlap_end:
                    # No overlap
                    new_ranges.append((start, end))
                    continue
                diff = src_start - dest_start
                result.append((overlap_start - diff, overlap_end - diff))
                if start < overlap_start < end:
                    new_ranges.append((start, overlap_start))
                if start < overlap_end < end:
                    new_ranges.append((overlap_end, end))
            ranges = new_ranges
        ranges = result + new_ranges

    return min(r[0] for r in ranges)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
