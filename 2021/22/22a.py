#!/usr/bin/env python3

# brute-force bitmap

import sys
import re
import numpy as np

MIN = -50
MAX =  50
N = MAX-MIN

A = np.zeros((N+1,N+1,N+1), dtype=int)
# print(A)

# translate [a,b] from left to 0
def translate(a, b, left):
    return a - left, b - left

def cap(a, b):
    a1 = max(a, 0)
    b1 = min(b, N)
    if a1 > N or b1 < 0:
        r = None
    else:
        r = (a1, b1)
    return r

# return cube intersected by (0..100, 0..100, 0..100)
def intersect(x1, x2, y1, y2, z1, z2):
    xrange, yrange, zrange = cap(x1, x2), cap(y1, y2), cap(z1, z2)
    if xrange == None or yrange == None or zrange == None:
        return ((0, -1), (0, -1), (0, -1))
    else:
        return (xrange, yrange, zrange)

def on(cube):
    xrange, yrange, zrange = cube
    for x in range(xrange[0], xrange[1] + 1):
        for y in range(yrange[0], yrange[1] + 1):
            for z in range(zrange[0], zrange[1] + 1):
                A[x,y,z] = 1

def off(cube):
    xrange, yrange, zrange = cube
    for x in range(xrange[0], xrange[1] + 1):
        for y in range(yrange[0], yrange[1] + 1):
            for z in range(zrange[0], zrange[1] + 1):
                A[x,y,z] = 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f.read().splitlines():
            if line:
                [x1, x2, y1, y2, z1, z2] = map(int, re.findall(r'[-]?\d+', line))
                # instead of -50..50, use 0..100
                x1, x2 = translate(x1, x2, MIN)
                y1, y2 = translate(y1, y2, MIN)
                z1, z2 = translate(z1, z2, MIN)
                if line[1] == "n":
                    on(intersect(x1, x2, y1, y2, z1, z2))
                else:
                    off(intersect(x1, x2, y1, y2, z1, z2))
        print(np.count_nonzero(A>0))
