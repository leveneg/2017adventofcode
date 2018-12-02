#! /usr/bin/env python3

import itertools
import sys


INPUT = [l.strip() for l in sys.stdin.readlines()]


def p1():
    return list(set(q.split(" ")[0]for q in INPUT)-set(q for k in INPUT for q in([]if "->" not in k else list(k.split("-> ")[1].split(", ")))))[0]

def p2():
    return (lambda a:lambda q,w:a(a,q,w))(lambda a,q,w:(w[q][1]and
        len({a(a,t,w)for t in w[q][1]})>1 and(return(w[[t for t in w[q][1]if a(a,t,w)!=max([a(a,t,w)for t in w[q][1]],key=[a(a,t,w)for t in w[q][1]].count)][0]][0]-(sum(a(a,t,w)for t in w[q][1])-len(w[q][1])*max([a(a,t,w)for t in w[q][1]],key=[a(a,t,w)for t in w[q][1]].count)))or __import__("sys").exit(0))or sum(a(a,t,w)for t in w[q][1])+w[q][0])or w[q][0])(list(set(q.split(" ")[0]for q in INPUT)-set(q for k in INPUT for q in([]if "->" not in k else list(k.split("-> ")[1].split(", ")))))[0],dict([(q.split(" ")[0], (int(q.split(" ")[1][1:-1]),[]if"->"not in q else list(q.split("-> ")[1].split(", "))))for q in INPUT]))

def main():
    print([p1(), p2()])


if __name__ == '__main__':
    main()

