#! /usr/bin/env python3


INPUT = 304


def solve(insertions):
    buff = [0]
    pos = 0

    for i in range(1, insertions + 1):
        pos = (pos + INPUT) % len(buff) + 1
        buff.insert(pos, i)

    return buff[pos + 1]

def p2():
    t = 0
    for i in range(1, 50000001):
        t = (t + INPUT) % i + 1
        if t == 1: r = i

    return r


def main():
    print([solve(2017), p2()])


if __name__ == '__main__':
    main()

