#! /usr/bin/env python3


from collections import defaultdict
import sys


INPUT = [l.strip() for l in sys.stdin.readlines()]


def solve(inp):
    groups = defaultdict(list)

    for line in inp:
        start, group = line.split(' <-> ')
        start = int(start)
        group = map(int, group.split(', '))

        for mem in group:
            groups[start].append(mem)
            groups[mem].append(start)

    def getGroup(prog):
        q = [prog]
        vis = set()

        while q:
            a = q.pop()
            for b in groups[a]:
                if b not in vis:
                    vis.add(b)
                    q.append(b)

        return vis

    p2 = 0
    s = set()

    for i in range(len(inp)):
        if i in s: continue

        p2 += 1
        s |= getGroup(i)

    return [len(getGroup(0)), p2]


def main():
    print(solve(INPUT))


if __name__ == '__main__':
    main()

