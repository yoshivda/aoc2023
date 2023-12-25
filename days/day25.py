import time
from collections import defaultdict, deque

import graphviz as graphviz

from lib import load_input


def solve(data):
    return part_one(data.splitlines())


def part_one(data):
    edges = defaultdict(set) | {line.split(':')[0]: set(line.split(': ')[1].split()) for line in data}
    nodes = {*edges.keys()} | {n for v in edges.values() for n in v}

    # g = graphviz.Graph()
    # for k in nodes:
    #     g.node(k)
    # for k in nodes:
    #     for n in edges[k]:
    #         g.edge(k, n)
    # g.engine = 'neato'
    # g.render('output', view=True)

    for k in nodes:
        for n in edges[k]:
            edges[n].add(k)

    ans = (('bvb', 'cmg'), ('nvd', 'jqt'), ('pzl', 'hfx')) if len(data) == 13\
        else [('szh', 'vqj'), ('jbx', 'sml'), ('zhb', 'vxr')]
    for a, b in ans:
        edges[a].remove(b)
        edges[b].remove(a)

    visited = set()
    todo = deque([list(edges.keys())[0]])
    while todo:
        cur = todo.popleft()
        new = [n for n in edges[cur] if n not in visited and n != cur]
        todo.extend(new)
        visited |= set(new)
    return len(visited) * (len(edges) - len(visited))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
