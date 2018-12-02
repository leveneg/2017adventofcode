#! /usr/bin/env python3


from collections import defaultdict
import sys


INPUT = [tuple(map(int, l.strip().split('/'))) for l in sys.stdin.readlines()]


def genBridges(lib, bridge=None):
    l, s, components, a = bridge or (0, 0, set(), 0)

    for b in lib[a]:
        n = (a, b) if a <= b else (b, a)
        if n not in components:
            new = l + 1, s + a + b, (components | {n}), b
            yield new; yield from genBridges(lib, new)


def solve():
    lib = defaultdict(set)
    for c in INPUT:
        a, b = c
        lib[a].add(b); lib[b].add(a)

    return [b[:2] for b in genBridges(lib)]


def main():
    bridges = solve()
    print([sorted(bridges, key=lambda x: x[1])[-1][1], sorted(bridges)[-1][1]])


if __name__ == '__main__':
    main()

