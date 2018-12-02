#! /usr/bin/env python3


from operator import add
import sys


INPUT = sys.stdin.readline().strip().split(',')
ORIGIN = (0, 0, 0)
MOVES = {
    'n':  ( 0,  1, -1),
    'ne': ( 1,  0, -1),
    'se': ( 1, -1,  0),
    's':  ( 0, -1,  1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0)
}


def solve(inp):
    p = ORIGIN[:]
    dist = furthest = 0

    for step in inp:
        p = tuple(map(add, p, MOVES[step]))
        dist = max(map(abs, p))
        furthest = max(dist, furthest)

    return [dist, furthest]

def main():
    assert solve(['ne', 'ne', 'ne'])[0] == 3
    assert solve(['ne', 'ne', 'sw', 'sw'])[0] == 0
    assert solve(['ne', 'ne', 's', 's'])[0] == 2
    assert solve(['se', 'sw', 'se', 'sw', 'sw'])[0] == 3

    print(solve(INPUT))


if __name__ == '__main__':
    main()

