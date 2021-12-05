#!/usr/bin/env python3
# Advent of Code 2021, Day 5
# Run it with ./5b.py data.txt

import sys
import numpy as np

N = 1000                        # from eyeballin' the datafile

a = np.zeros([N,N], dtype=int)

def drawline(x0, y0, x1, y1):
    global a
    # lines are either horizontal, vertical or diagonal
    # sort endpoints so that we go from left to right (increasing x)
    if x0 > x1:                  # 9,7 -> 7,9 ==> 7,9 -> 9,7
        x0,y0,x1,y1 = x1,y1,x0,y0
    # make vertical lines go by increasing y
    if (x0 == x1) and (y0 > y1):
        x0,y0,x1,y1 = x0,y1,x1,y0
    # make horizontal lines go by increasing x
    if (y0 == y1) and (x0 > x1):
        x0,y0,x1,y1 = x1,y0,x0,y1
    if x0 == x1:                # vertical line
        a[x0,y0:y1+1] += 1
    elif y0 == y1:              # horizontal line
        a[x0:x1+1,y0] += 1
    else:                       # diagonal line (but don't know if y0 < y1)
        dy = 1
        if y0 > y1:
            dy = -1
        for x in range(x0,x1+1):
            a[x,y0+(x-x0)*dy] += 1

if __name__ == "__main__":
    list = open(sys.argv[1]).readlines()
    for p in list:
        y0 = int(p.split("->")[0].split(",")[0])
        x0 = int(p.split("->")[0].split(",")[1])
        y1 = int(p.split("->")[1].split(",")[0])
        x1 = int(p.split("->")[1].split(",")[1])
        drawline(x0, y0, x1, y1)
    print(np.count_nonzero(a>1))
