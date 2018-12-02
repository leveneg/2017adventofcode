#! /usr/bin/env python3


import sys


INPUT = [c for c in sys.stdin.readline().strip()]
#INPUT = '{{<a!>},{<a!>},{<a!>},{<ab>}}'


def solve():
    score = level = garbo = 0
    ignoreNext = inGarbage = False

    for c in INPUT:
        #print('c: {}, inGarbage: {}, ignoreNext: {}'.format(c, inGarbage, ignoreNext))

        if ignoreNext and inGarbage:
            ignoreNext = False
            continue

        if inGarbage and c != '>':
            if c == '!': ignoreNext = True
            else: garbo += 1

            continue

        if c == '{': level += 1
        elif c == '}': score += level; level -= 1
        elif c == '<': inGarbage = True
        elif c == '>': inGarbage = False
        elif c == '!': ignoreNext = True


    return([score, garbo])

def main():
    print(solve())


if __name__ == '__main__':
    main()

