#! /usr/bin/env python3


def solve():
    factors = [16807, 48271]
    seeds = [634, 301]
    divisors = [4, 8]
    d = 2147483647
    p1 = p2 = 0

    def getGen(seed, factor, mult=1):
        x = seed
        while True:
            x = (x * factor) % d
            if x % mult == 0:
                yield x

    def isMatching(generators):
        return len(set(map(lambda x: bin(next(x))[-16:], generators))) == 1

    gens = [getGen(s, f) for s, f in zip(seeds, factors)]

    for i in range(40000000):
        if isMatching(gens): p1 += 1

    gens = [getGen(s, f, b) for s, f, b in zip(seeds, factors, divisors)]

    for i in range(5000000):
        if isMatching(gens): p2 += 1

    return [p1, p2]


def main():
    print(solve())


if __name__ == '__main__':
    main()

