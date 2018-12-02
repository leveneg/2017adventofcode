#! /usr/bin/env python3


import sys
from collections import defaultdict


INPUT = [l.strip() for l in sys.stdin.readlines()]


class Particle(object):
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a


    def step(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]


    def dist(self):
        return sum([abs(x) for x in self.p])


def solve(raw):
    parts = {}
    for i, pLine in enumerate(raw):
        parts[i] = Particle(*[[int(c) for c in a[3:-1].split(',')] for a in pLine.split(', ')])

    damp = p1 = p2 = 0
    while True:
        minD = None
        minPart = None

        for i, part in parts.items():
            part.step()
            d = part.dist()

            if minD is None or d < minD:
                minPart = i
                minD = d

        posDict = defaultdict(list)
        for i, part in parts.items():
            k = tuple(part.p)
            posDict[k].append(i)

        for k, v in posDict.items():
            if len(v) > 1:
                for i in v:
                    del parts[i]

        p2 = len(parts)


        if minPart == p1:
            damp += 1
        else:
            p1 = minPart

        if damp >= 1000:
            return [p1, p2]


def main():
    print(solve(INPUT))


if __name__ == '__main__':
    main()

