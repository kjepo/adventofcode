#!/usr/bin/env python3

import sys
from copy import copy, deepcopy

MAX = 10

# recursively expand area around (y,x) until we hit 9
def basin(y,x):
    global basincount
    if basins[y][x] >= 9 or basins[y][x] == -1:
        return
    basincount = basincount + 1
    basins[y][x] = -1
    basin(y-1,x)
    basin(y+1,x)
    basin(y,x-1)
    basin(y,x+1)

heightmap = []
xdim = None
if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    for line in lines:
        heights = [MAX] + [int(c) for c in line.strip()] + [MAX]
        if not xdim:
            xdim = len(heights) - 2
            heightmap.append((xdim+2)*[MAX])
        heightmap.append(heights)
    heightmap.append((xdim+2)*[MAX])
ydim = len(heightmap) - 2
basincounts = []
basins = deepcopy(heightmap)
for y in range(1,ydim+1):
    for x in range(1,xdim+1):
        z  = heightmap[y][x]
        zn = heightmap[y-1][x+0]
        zs = heightmap[y+1][x+0]
        zw = heightmap[y+0][x-1]
        ze = heightmap[y+0][x+1]
        basincount = 0
        if z < zn and z < zs and z < zw and z < ze:
            basin(y, x)
        if basincount > 0:
            basincounts.append(basincount)

"""
for row in basins:    # if you want to see a pretty print of basins
    for b in row:
        print(str(b).rjust(5), end="")
    print()
"""

basincounts.sort()              # grossly inefficient but...
basincounts.reverse()           # this too (sorry)
if len(basincounts) > 2:
    print(basincounts[0],  basincounts[1],  basincounts[2])
    print(basincounts[0] * basincounts[1] * basincounts[2])
