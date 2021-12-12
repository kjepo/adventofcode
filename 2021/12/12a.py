#!/usr/bin/env python3

import sys

edges = []
nodes = []

def big(cave):
    return cave[0] >= 'A' and cave[0] <= 'Z'

def bfs(paths):
    finished = False
    while not finished:
        finished = True
        for p in paths[:]:      # try to augment each path p=[start,...,x]
            fringe = p[-1]
            if fringe == 'end': # unless x != end
                continue
            for (a,b) in edges:
                if fringe == a:
                    if not b in p or big(b):
                        if not(p + [b] in paths):
                            paths.append(p + [b])
                            finished = False
    c = 0
    for p in paths:
        if p[-1] == 'end':
            c += 1
    return c

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    for line in lines:
        [node1,node2] = line.strip().split("-")
        edges.append((node1, node2))
        edges.append((node2, node1))
        if not node1 in nodes:
            nodes.append(node1)
        if not node2 in nodes:
            nodes.append(node2)
    print("-->", bfs([['start']]))
    
