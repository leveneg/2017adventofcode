#! /usr/bin/env python3


import sys


INPUT = [l for l in sys.stdin.readlines()]


def solve(diagram):
    sym = '|'
    p = (diagram[0].index(sym), 0)
    d = (0, 1)
    letters = []
    steps = 0

    while sym != ' ':
        steps += 1
        p = tuple(map(sum, zip(p, d)))
        sym = diagram[p[1]][p[0]]

        if sym == '+':
            if d[1] != 0:
                d = (-1, 0) if diagram[p[1]][p[0]-1] != ' ' else (1, 0)
            else:
                d = (0, -1) if diagram[p[1]-1][p[0]] != ' ' else (0, 1)
        elif sym not in ('|', '-'):
            letters.append(sym)

    return [''.join(letters), steps]


def main():
    print(solve(INPUT))


if __name__ == '__main__':
    main()

