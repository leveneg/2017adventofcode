#! /usr/bin/env python3

from string import ascii_lowercase as letters
import sys

INPUT = sys.stdin.read().strip().split(',')

def solve():
    line = list(letters[:16])
    l = len(line)

    seen = []
    for i in range(1000000000):
        s = ''.join(line)
        if s in seen: return seen[1000000000 % i]
        seen.append(s)

        for move in INPUT:
            if move[0] == 's':
                n = int(move[1:])
                line = line[-n:] + line[:-n]
            elif move[0] == 'x':
                a, b = map(int, move[1:].split('/'))
                line[a], line[b] = line[b], line[a]
            elif move[0] == 'p':
                a, b = map(lambda x: line.index(x), move[1:].split('/'))
                line[a], line[b] = line[b], line[a]
            else:
                raise Exception

    return ''.join(line)

def main():
    print(solve())


if __name__ == '__main__':
    main()

