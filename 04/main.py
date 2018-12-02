#! /usr/bin/env python3

import sys


INPUT = [l.strip().split() for l in sys.stdin.readlines()]


def p1():
    return sum(len(r) == len(set(r)) for r in INPUT)


def p2():
    return sum(len(r) == len(set(''.join(sorted(w)) for w in r)) for r in INPUT)


def main():
    print([p1(), p2()])


if __name__ == '__main__':
    main()

