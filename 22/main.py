#! /usr/bin/env python3


from collections import defaultdict
import sys


INIT = [list(l.strip()) for l in sys.stdin.readlines()]


def p1():
    m = INIT[:]
    p = (len(m[0]) // 2, len(m) // 2)
    d = (0, -1)
    outliers = defaultdict(lambda: '.')

    result = 0

    for _ in range(10000):

        isOnMap = all(map(lambda x: 0 <= x < len(m), p))
        sym = m[p[1]][p[0]] if isOnMap else outliers[p]
        newSym = '.' if sym == '#' else '#'
        d = (-d[1], d[0]) if sym == '#' else (d[1], -d[0])

        if isOnMap:
            m[p[1]][p[0]] = newSym
        else:
            outliers[p] = newSym

        if newSym == '#': result += 1

        p = tuple(a+b for a, b in zip(p, d))

    for i, row in enumerate(m):
        print('{:2}: '.format(i) + ''.join(row))

    return result

def p2():
    # _doesn't
    m = INIT[:]
    p = (len(m[0]) // 2, len(m) // 2)
    d = (0, -1)
    outliers = defaultdict(lambda: '.')
    dirs = {
        '.': lambda x, y: (y, -x),
        'W': lambda x, y: (x, y),
        '#': lambda x, y: (-y, x),
        'F': lambda x, y: (-x, -y)
    }
    states = list(dirs.keys())
    numStates = len(states)

    result = 0

    for _ in range(10000000):
        isOnMap = all(map(lambda x: 0 <= x < len(m), p))
        sym = m[p[1]][p[0]] if isOnMap else outliers[p]
        newSym = states[(states.index(sym) + 1) % numStates]
        print('p: {}, sym: {} => {}, d: {}'.format(p, sym, newSym, d))
        d = dirs[sym](*d)

        if isOnMap:
            m[p[1]][p[0]] = newSym
        else:
            outliers[p] = newSym

        if newSym == '#': result += 1

        p = tuple(a+b for a, b in zip(p, d))

    for i, row in enumerate(m):
        print('{:2}: '.format(i) + ''.join(row))

    return result



def main():
    print([p1(), p2()])


if __name__ == "__main__":
    main()
