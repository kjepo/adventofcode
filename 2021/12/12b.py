#!/usr/bin/env python3

import sys

edges = []
nodes = []

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
    # We know that cave appears in path[:-1] already: assert(cave, path[:-1])
    # Question is: is there already an p in path that appears twice?

    count = { }
    for p in nodes:
        count[p] = 0
    for p in path:
        if not big(p):
            count[p] += 1
            if count[p] == 2:
                return False

    # Guess not, so allow it
    return True
    

def bfs(paths):
    finished = False
    while not finished:
        print(len(paths))
        finished = True
        for p in paths[:]:
            fringe = p[-1]
            if fringe == 'end': # unless x != end
                continue
            for (a,b) in edges: # try to augment path=[..., fringe] with b
                if fringe == a and legit(p, b):
                    if not p + [b] in paths:
                        paths.append(p + [b])
                        finished = False
    count = 0
    for p in paths:
        if p[-1] == 'end':
            count += 1
    return count

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
    
