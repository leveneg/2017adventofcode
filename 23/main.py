#! /usr/bin/env python3


from collections import defaultdict
import sys


INPUT = [l.strip().split(' ') for l in sys.stdin.readlines()]


def p1():
    instructions = INPUT[:]
    regs = defaultdict(int)
    commands = {
        'set': lambda _, y: y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y
    }

    def getVal(val):
        try:
            return int(val)
        except ValueError:
            return regs[val]

    idx = result = 0

    while 0 <= idx < len(instructions):
        op, x, y = instructions[idx]

        if op == 'jnz':
            idx += getVal(y) - 1 if getVal(x) else 0
        elif op in ['set', 'sub', 'mul']:
            regs[x] = commands[op](regs[x], getVal(y))

        if op == 'mul':
            result += 1

        idx += 1

    return result


# ended up just having to disassemble the program to sort this out
def p2():
    h = 0
    for i in range(108400, 125400 + 1, 17):
        for x in range(2, i):
            if i % x == 0:
                h += 1
                break

    return h


def main():
    print([p1(), p2()])


if __name__ == "__main__":
    main()
