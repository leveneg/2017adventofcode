#! /usr/bin/env python3


from collections import defaultdict
import operator
import sys
import time


INPUT = [l.strip().split() for l in sys.stdin.readlines()]


def solve(instructions):
    regs = defaultdict(int)
    regs2 = defaultdict(int)
    regs2['p'] = 1
    progs = [regs, regs2]
    p = 0
    freq = None

    def getVal(val):
        try:
            return int(val)
        except ValueError:
            return regs[val]

    idx = 0
    while 0 <= idx < len(instructions):
        ins = instructions[idx]
        op, *opr = ins

        if op in ['add', 'mul', 'mod']:
            reg, val = opr
            regs[reg] = getattr(operator, op)(regs[reg], getVal(val))
        elif op == 'set':
            reg, val = opr
            regs[reg] = getVal(val)
        elif op == 'snd':
            freq = getVal(opr[0])
        elif op == 'rcv':
            if opr[0] != 0: return freq
        elif op == 'jgz':
            val, offset = opr
            idx += (int(offset) - 1) if getVal(val) > 0 else 0

        idx += 1


def main():
    print(solve(INPUT))


if __name__ == '__main__':
    main()

