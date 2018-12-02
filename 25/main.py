#! /usr/bin/env python3


BP = {
    'a': [(1, 1, 'b'), (0, -1, 'c')],
    'b': [(1, -1, 'a'), (1, 1, 'd')],
    'c': [(1, 1, 'a'), (0, -1, 'e')],
    'd': [(1, 1, 'a'), (0, 1, 'b')],
    'e': [(1, -1, 'f'), (1, -1, 'c')],
    'f': [(1, 1, 'd'), (1, 1, 'a')]
}


def solve():
    idx = 0
    tape = {}
    state = 'a'

    for i in range(12173597):
        wr, mv, state = BP[state][tape.get(idx, 0)]
        tape[idx] = wr
        idx += mv

    return sum(tape.values())


def main():
    print([solve()])


if __name__ == '__main__':
    main()
