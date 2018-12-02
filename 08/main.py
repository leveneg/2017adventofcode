#! /usr/bin/env python3

import operator as op
import sys


INPUT = [l.strip() for l in sys.stdin.readlines()]


WORDS = {
    "inc": op.add,
    "dec": op.sub,
    "<": op.lt,
    "<=": op.le,
    "==": op.eq,
    ">": op.gt,
    ">=": op.ge,
    "!=": op.ne
}


def solve():
    regs = {}
    top = 0

    for ins in INPUT:
        reg, f, n, _, lhsReg, comp, rhs = ins.split(" ")

        o = regs.get(reg, 0)
        lhs = regs.get(lhsReg, 0)
        fFunc = WORDS[f]
        compFunc = WORDS[comp]

        regs[reg] = fFunc(o, int(n)) if compFunc(lhs, int(rhs)) else o
        top = regs[reg] if regs[reg] > top else top

    return [max(regs.values()), top]

def main():
    print(solve())


if __name__ == '__main__':
    main()

