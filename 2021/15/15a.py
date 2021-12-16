#!/usr/bin/env python3
# Advent of Code 2021, Day 5
# Run it with ./5b.py data.txt

import sys

MAX = sys.maxsize
A = { } # A[x,y] 

# Adjacency graph representation
# each node (x,y) can reach 2, 3, or 4 nodes (x-1,y), (x+1,y), (x,y-1), (x,y+1)
# weight of each node is the cost of going there
# so an edge (x,y) -- (x+1,y) has the weight A[x+1,y]


def construct_neighbors():
    neighbor = { }
    for x in range(N):
        for y in range(N):
            next = []
            if x > 0:
                next.append((x-1,y))
            if y > 0:
                next.append((x,y-1))
            if x < N-1:
                next.append((x+1,y))
            if y < N-1:
                next.append((x,y+1))
            neighbor[x,y] = next
    return neighbor
    
def findmin(q, d):
    best = q[0]
    for u in q:
        if d[u] < d[best]:
            best = u
    return best

def weight(u,v):
    return A[v]

def dijkstra(source):
    neighbor = construct_neighbors()
    # list of vertices
    vertices = queue = [(x,y) for x in range(N) for y in range(N)]
    # shortest path estimation
    d = { }
    for v in vertices:
        d[v] = sys.maxsize
    d[source] = 0
    s = []
    while len(queue) > 0:
        u = findmin(queue, d)
        queue.remove(u)
        s.append(u)
        for v in neighbor[u]:
            if d[v] > d[u] + A[v]:
                d[v] = d[u] + A[v]
    return d

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    y = 0
    for line in lines:
        line = line.strip()
        x = 0
        for c in line:
            A[x,y] = int(c)
            x += 1
        y = y + 1
    N = y
    print("Problem size:", N, end=' ')
    d = dijkstra((0, 0))
    print("-->", d[N-1,N-1])
    
