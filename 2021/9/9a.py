#!/usr/bin/env python3

import sys

# To make comparisons easier we add a frame around the 2D array,
# filled with maxints.

MAX = 10

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
lowpoints = []
for y in range(1,ydim+1):
    for x in range(1,xdim+1):
        z = heightmap[y][x]
        zn = heightmap[y-1][x+0]
        zs = heightmap[y+1][x+0]
        zw = heightmap[y+0][x-1]
        ze = heightmap[y+0][x+1]
        if z < zn and z < zs and z < zw and z < ze:
            lowpoints.append(1+z)

"""
for row in heightmap:    # if you want to see a pretty print of heightmap
    for b in row:
        print(str(b).rjust(5), end="")
    print()
"""

print(sum(lowpoints))
