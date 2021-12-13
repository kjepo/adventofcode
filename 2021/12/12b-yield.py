#!/usr/bin/env python3
import sys

# 12B solved with another data structure and using Python generators
# This only takes a few seconds, I'm guessing because of the data structure.

G = { }   # G[u] = all nodes v such that u-v is an edge in the graph

def big(cave):
    return cave[0] >= 'A' and cave[0] <= 'Z'

def legit(path, cave):
    # we can always go to the end node
    if cave == 'end':
        return True
    # never go back to start node
    if cave == 'start':
        return False
    # big caves can always be visited
    if big(cave):
        return True
    # simple case: if never encountered, accept it
    if cave not in path:
        return True

    # A path must not have more than one cave that appears twice
    # We know that cave appears in path already.
    # Question is: is there already an p in path that appears twice?

    assert(cave in path);

    count = { }
    for p in G:
        count[p] = 0
    for p in path:
        if not big(p):
            count[p] += 1
            if count[p] == 2:
                return False

    # Guess not, so allow it
    return True

def dfs(u, path):
    if u == 'end':
        yield path + [u]
    else:
        for v in G[u]:
            if legit(path + [u], v):
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
