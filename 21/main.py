#! /usr/bin/env python3


from collections import defaultdict
import sys


INIT = '.#./..#/###'
RULES = {k: v for k, v in (l.strip().split(' => ') for l in sys.stdin.readlines())}


# str : str
def sqToStr(sq, sz):
    return '/'.join([''.join(sq)[i:i+sz] for i in range(0, len(sq), sz)])


# str : list(str)
def splitImg(imgStr):
    lines = imgStr.split('/')
    sz = 2 if len(lines) % 2 == 0 else 3
    squares = defaultdict(list)

    for i, line in enumerate(lines):
        l = len(line)
        for j, px in enumerate(line):
            idx = (l * (i // sz)) + (j // sz)
            squares[idx].append(px)

    cats = map(''.join, squares.values())

    return [sqToStr(s, sz) for s in cats]


# list(str) : str
def reassembleImg(squares):
    img = defaultdict(list)
    rt = len(squares) ** 0.5
    sz = 2 if len(squares) % 2 == 0 else 3

    for i, sq in enumerate(squares):
        rows = sq.split('/')
        l = len(rows)
        for j, row in enumerate(rows):
            idx = (l * (i // rt)) + j
            img[idx].extend(row)

    return '/'.join([''.join(r) for r in img.values()])


# str : gen(str)
def genTranslations(sqrStr):
    lines = sqrStr.split('/')
    sz = len(lines)

    for i in range(8):
        lines = [''.join(p) for p in zip(*lines)] if i % 2 else lines[::-1]

        yield sqToStr(''.join(lines), sz)


def solve(iters):
    img = INIT[:]

    for _ in range(iters):
        acc = []
        squares = splitImg(img)

        for sq in squares:

            for t in genTranslations(sq):
                if RULES.get(t, None):
                    acc.append(RULES[t])
                    break
            else:
                raise Exception("Rule not found!")

        img = reassembleImg(acc)

    return sum(1 for c in img if c == '#')


def main():
    print([solve(5), solve(18)])


if __name__ == "__main__":
    main()
