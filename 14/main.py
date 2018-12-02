#! /usr/bin/env python3


from functools import reduce
from operator import xor
import sys


INPUT = 'hwlqcszp'
SALT = [17, 31, 73, 47, 23]


def once(string, lengths, idx = 0, skip = 0):
    strlen = len(string)

    for l in lengths:
        r = []

        for x in range(l):
            n = (idx + x) % strlen
            r.append(string[n])

        r.reverse()

        for x in range(l):
            n = (idx + x) % strlen
            string[n] = r[x]

        idx = (idx + l + skip) % strlen
        skip += 1

    return(string, idx, skip)


def condense(string):
    dense = []

    for x in range(16):
        ss = string[x * 16: (x * 16) + 16]
        dense.append('{:02x}'.format(reduce(xor, ss)))

    return(''.join(dense))


def knotHash(inp):
    idx = skip = 0
    string = [n for n in range(256)]
    lengths = [ord(l) for l in inp] + SALT

    for _ in range(64):
        string, idx, skip = once(string, lengths, idx, skip)

    return(condense(string))


def solve(inp):
    rows = [[int(d) for d in list(bin(int(knotHash('{}-{}'.format(inp, n)), 16))[2:].zfill(128))] for n in range(128)]

    ones = []
    for j, r in enumerate(rows):
        ones += [(j, k) for k, d in enumerate(r) if d]

    p1 = len(ones)
    p2 = 0

    while ones:
        q = [ones[0]]

        while q:
            (x, y) = q.pop()

            if (x, y) in ones:
                ones.remove((x, y))
                q += [(x-1, y), (x+1,y), (x,y-1), (x,y+1)]

        p2 += 1

    return [p1, p2]


def main():
    print(solve(INPUT))


if __name__ == '__main__':
    main()

