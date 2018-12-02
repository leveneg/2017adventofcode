#! /usr/bin/env python3


from functools import reduce
from operator import xor
import sys


INPUT = sys.stdin.readline().strip()
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


def p1():
    base = [n for n in range(256)]
    res, _, _ = once(base, [int(l) for l in INPUT.split(',')])

    return(res[0] * res[1])


def p2():
    return knotHash(INPUT)


def main():
    assert knotHash("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert knotHash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert knotHash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert knotHash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

    print([p1(), p2()])


if __name__ == '__main__':
    main()

