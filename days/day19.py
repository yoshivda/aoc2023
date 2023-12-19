import re
from math import prod

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n')[0].splitlines())


def part_one(data):
    wfs = {line.split('{')[0]: [rule.split(':') for rule in line.split('{')[1][:-1].split(',')] for line in data[0].splitlines()}
    return sum(process(wfs, 'in', *(int(x) for x in re.findall(r'\d+', line))) for line in data[1].splitlines())


def process(wfs, name, x, m, a, s):
    wf = wfs[name]
    for rule in wf:
        if len(rule) == 1:
            res = rule[0]
        elif eval(rule[0]):
            res = rule[1]
        else:
            continue
        if res == 'A':
            return x + m + a + s
        if res == 'R':
            return 0
        return process(wfs, res, x, m, a, s)


def part_two(data):
    wfs = {line.split('{')[0]: [rule.split(':') for rule in line.split('{')[1][:-1].split(',')] for line in data}
    return check(wfs, 'in', {f'{c}min': 1 for c in 'xmas'} | {f'{c}max': 4001 for c in 'xmas'})


def check(wfs, name, minmax):
    if name == 'A':
        return prod(minmax[f'{c}max'] - minmax[f'{c}min'] for c in 'xmas')
    elif name == 'R':
        return 0
    wf = wfs[name]
    res = 0
    for rule in wf:
        if len(rule) == 1:
            res += check(wfs, rule[0], minmax)
            continue
        l, s = rule[0][:2]
        num = int(rule[0][2:])
        if s == '<' and minmax[f'{l}min'] < num:
            res += check(wfs, rule[1], minmax | {f'{l}max': min(minmax[f'{l}max'], num)})
            minmax[f'{l}min'] = num
        elif s == '>' and minmax[f'{l}max'] > num + 1:
            res += check(wfs, rule[1], minmax | {f'{l}min': max(minmax[f'{l}min'], num + 1)})
            minmax[f'{l}max'] = num + 1
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
