#!/usr/bin/env python3

import sys
import numpy as np

tr = { b'v': "v", b'>': ">", b'.': "." }

def P(map):
    ydim, xdim = map.shape
    for y in range(ydim):
        for x in range(xdim):
            print(tr[map[y,x]], end='')
        print()

def next(x, y, dx, dy, xdim, ydim):
    if dx == 1 and dy == 0:
        if x < xdim-1:
            return x+dx, y+dy
        else:
            return 0, y+dy
    elif dx == 0 and dy == 1:
        if y < ydim-1:
            return x+dx, y+dy
        else:
            return x+dx, 0
    else:
        print("next: shouldn't happen")
        exit(0)

def move(dx, dy, map):
    change = False
    map2 = np.copy(map)
    ydim, xdim = map.shape
    for y in range(ydim):
        for x in range(xdim):
            nx, ny = next(x, y, dx, dy, xdim, ydim)
            if dx == 1 and map[y,x] == b'>' and map[ny,nx] == b'.':
                map2[y,x] = b'.'
                map2[ny,nx] = b'>'
                change = True
            elif dy == 1 and map[y,x] == b'v' and map[ny,nx] == b'.':
                map2[y,x] = b'.'
                map2[ny,nx] = b'v'
                change = True
    return map2, change

if __name__ == "__main__":
    map = np.genfromtxt(sys.argv[1], dtype='c', delimiter=1)
    i, change1, change2 = 0, True, True
    while change1 or change2:
        map, change1 = move(1, 0, map)
        map, change2 = move(0, 1, map)
        i = i + 1
    # P(map)
    print("reached fixed point after", i, "iterations")
