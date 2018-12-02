#! /usr/bin/env python3

import itertools
import sys


INPUT = [int(l) for l in sys.stdin.readline().split()]


def p1():
    inp = INPUT[:]
    sets = []

    while inp not in sets:
        sets.append(inp[:])
        m = max(inp)
        i = inp.index(m)
        inp[i] = 0

        while m:
            i = (i + 1) % len(inp)
            inp[i] += 1
            m -= 1

    return len(sets), len(sets) - sets.index(inp)

def main():
    print(list(p1()))


if __name__ == '__main__':
    main()

