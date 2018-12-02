#! /usr/bin/env python3

import sys

CAPTCHA = sys.stdin.readline().strip()
CAPLEN = len(CAPTCHA)

def solve(steps):
    sums = [0 for _ in steps]

    def isEqual(idx, step):
        return(CAPTCHA[idx] == CAPTCHA[(idx + step) % CAPLEN])

    for i, c in enumerate(CAPTCHA):
        for j, s in enumerate(steps):
            sums[j] = sums[j] + int(c) if isEqual(i, s) else sums[j]

    return(sums)


def main():
    steps = [1, CAPLEN // 2]
    print(solve(steps))


if __name__ == '__main__':
    main()
