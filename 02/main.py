#! /usr/bin/env python3

from itertools import permutations
import sys

INPUT = [[int(n) for n in l.strip().split('\t')] for l in sys.stdin.readlines()]


def p1():
    return sum([max(r) - min(r) for r in INPUT])


def p2():
    return sum(p//q for r in INPUT for p,q in permutations(r, 2) if p%q == 0)


def main():
    print([p1(), p2()])


if __name__ == '__main__':
    main()
