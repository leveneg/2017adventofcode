#! /usr/bin/env python3

import sys


INPUT = [int(l.strip()) for l in sys.stdin.readlines()]


def p1():
    p1Input = INPUT[:]
    idx = count = 0

    while -1 < idx < len(p1Input):
        nIdx = idx + p1Input[idx]
        p1Input[idx] += 1
        idx = nIdx
        count += 1

    return count

def p2():
    p2Input = INPUT[:]
    idx = count = 0

    while -1 < idx < len(p2Input):
        nIdx = idx + p2Input[idx]

        if p2Input[idx] > 2:
            p2Input[idx] -= 1
        else:
            p2Input[idx] += 1

        idx = nIdx
        count += 1

    return count

def main():
    print([p1(), p2()])


if __name__ == '__main__':
    main()

