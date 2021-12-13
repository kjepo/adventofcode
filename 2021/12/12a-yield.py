#!/usr/bin/env python3
import sys

# 12A solved with another data structure and using Python generators

G = { }   # G[u] = all nodes v such that u-v is an edge in the graph

def big(cave):
    return cave[0] >= 'A' and cave[0] <= 'Z'

def dfs(u, path):
    if u == 'end':
        yield path + [u]
    else:
        for v in G[u]:
            if big(v) or v not in path + [u]:
                yield from dfs(v, path + [u])

if __name__ == "__main__":
    for line in open(sys.argv[1]).readlines():
        [u,v] = line.strip().split("-")
        if u not in G:
            G[u] = []
        if v not in G:
            G[v] = []
        G[u].append(v)
        G[v].append(u)
    print(len(list(dfs('start', []))))
