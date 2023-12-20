from collections import deque, defaultdict
from math import lcm

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    pulses = deque()
    modules = dict()
    inputs = defaultdict(dict)
    init = []
    lo = hi = 0
    for line in data:
        module, dests = line.split(' -> ')
        dests = dests.split(', ')
        if module == 'broadcaster':
            init = [(dest, False, 'broadcaster') for dest in dests]
        else:
            modules[module[1:]] = [module[0], False, dests]
        for dest in dests:
            inputs[dest][module[1:]] = False

    for _ in range(1000):
        pulses.extend(init)
        lo += 1
        while pulses:
            receiver, high, sender = pulses.popleft()
            if high:
                hi += 1
            else:
                lo += 1
            if receiver not in modules:
                continue
            inputs[receiver][sender] = high
            ty, on, dests = modules[receiver]
            if ty == '%' and not high:
                pulses.extend((dest, not on, receiver) for dest in dests)
                modules[receiver][1] = not on
            elif ty == '&':
                pulses.extend((dest, not all(inputs[receiver].values()), receiver) for dest in dests)
    return lo * hi


def part_two(data):
    pulses = deque()
    modules = dict()
    inputs = defaultdict(dict)
    init = []
    lo = hi = 0
    for line in data:
        module, dests = line.split(' -> ')
        dests = dests.split(', ')
        if module == 'broadcaster':
            init = [(dest, False, 'broadcaster') for dest in dests]
        else:
            modules[module[1:]] = [module[0], False, dests]
        for dest in dests:
            inputs[dest][module[1:]] = False
    i = 0
    periods = dict()
    while len(periods.values()) < 4:
        i += 1
        pulses.extend(init)
        lo += 1
        while pulses:
            receiver, high, sender = pulses.popleft()
            if receiver == 'lg' and high and sender not in periods:
                periods[sender] = i
            if high:
                hi += 1
            else:
                lo += 1
            if receiver not in modules:
                continue
            inputs[receiver][sender] = high
            ty, on, dests = modules[receiver]
            if ty == '%' and not high:
                pulses.extend((dest, not on, receiver) for dest in dests)
                modules[receiver][1] = not on
            elif ty == '&':
                pulses.extend((dest, not all(inputs[receiver].values()), receiver) for dest in dests)
    return lcm(*periods.values())


if __name__ == '__main__':
    # print(solve(load_input('small')))
    # print(solve(load_input('small2')))
    print(solve(load_input()))
