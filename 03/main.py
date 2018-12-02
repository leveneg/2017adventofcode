#! /usr/bin/env python3


"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""


INPUT = 277678


def p1():
    idx = -(-INPUT ** 0.5 // 1)
    idx = idx if idx % 2 else idx + 1

    toCenter = (idx - 1) // 2
    axis = [idx ** 2 - ((idx) - 1) * i - (idx // 2) for i in range(0, 4)]
    steps = min([abs(a - INPUT) for a in axis])

    return toCenter + steps


def p2():
    pass


def main():
    print([p1(), p2()])


if __name__ == '__main__':
    main()

