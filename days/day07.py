from collections import Counter

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum((i + 1) * int(t[2]) for i, t in
               enumerate(sorted([(score(line.split()[0]), *line.split()) for line in data],
                                key=lambda t: (t[0], tuple('23456789TJQKA'.index(c) for c in t[1])))))


def score(hand):
    freqs = Counter(hand)
    if max(freqs.values()) == 5:
        return 7
    elif max(freqs.values()) == 4:
        return 6
    elif max(freqs.values()) == 3:
        if len(freqs.values()) == 2:
            return 5
        else:
            return 4
    elif sum(i == 2 for i in freqs.values()) == 2:
        return 3
    elif max(freqs.values()) == 2:
        return 2
    return 1


def part_two(data):
    return sum((i + 1) * int(t[2]) for i, t in
               enumerate(sorted([(
                   score(line.split()[0].replace('J', Counter(line.replace('J', '').split()[0]).most_common(1)[0][0])),
                   *line.split()) for line in data],
                                key=lambda t: (t[0], tuple('J23456789TQKA'.index(c) for c in t[1])))))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
