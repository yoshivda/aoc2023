import re
from functools import reduce

from lib import load_input


def solve(data):
    # return part_one(data)
    return part_two(data)


def part_one(data):
    return sum(reduce(lambda x, y: ((x + ord(y)) * 17) % 256, word, 0)
               for word in data.strip().split(','))


def hash(word):
    val = 0
    for c in word:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def part_two(data):
    mem = [[] for _ in range(256)]
    for text in data.strip().split(','):
        label = re.search(r'\w+', text).group()
        hsh = hash(label)
        if '-' in text:
            index = -1
            for i, (lbl, val) in enumerate(mem[hsh]):
                if lbl == label:
                    index = i
                    break
            if index >= 0:
                mem[hsh].pop(index)
        elif '=' in text:
            fl = int(text[text.index('=') + 1:])
            index = -1
            for i, (lbl, val) in enumerate(mem[hsh]):
                if lbl == label:
                    index = i
                    break
            if index >= 0:
                mem[hsh][index] = (label, fl)
            else:
                mem[hsh].append((label, fl))
    return sum((i + 1) * (j + 1) * fl for i, box in enumerate(mem) for j, (_, fl) in enumerate(box))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
