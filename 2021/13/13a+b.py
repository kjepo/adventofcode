#!/usr/bin/env python3

# Solution to day 13
# Use the following for answer to 1st part:
#
# ./13a.py data.txt | grep dots | head -1
#
# Use the following for answer to 2nd part
#
# ./13a.py data.txt

# Possible ambiguity?
#
#   fold at x=3 with 6 dots along x-axis
#        |
#     ....##   => ##..##  => ##.     ?
#              => ###.##  => ###     ?
#

import sys

grid = { }
xmax, ymax = 0, 0               # initial dimensions
xaxis, yaxis = 0, 0             # current dimensions

def foldx(atx):
    global xaxis
    for y in range(yaxis+1):
        for x in range(xaxis+1):
            if (x,y) in grid and x > atx:
                grid[(2*atx-x, y)] = '#'
    xaxis = atx - 1

def foldy(aty):
    global yaxis    
    for y in range(yaxis+1):
        for x in range(xaxis+1):
            if (x,y) in grid and y > aty:
                grid[x, (2*aty-y)] = '#'                
    yaxis = aty - 1

def pr():
    c = 0
    for y in range(yaxis+1):
        for x in range(xaxis+1):
            if (x,y) in grid:
                print('#', end='')
                c += 1
            else:
                print('.', end='')
        print()
    print("-->", c, "dots")
    print()

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    for line in lines:
        line = line.strip()
        if "fold along x=" in line:      # fold along x=42
            x = int(line.split("=")[1])
            foldx(x)
            pr()
        elif "fold along y=" in line:    # fold along y=17
            y = int(line.split("=")[1])
            foldy(y)
            pr()
        elif line:                       # 4711,256
            x = int(line.split(",")[0])
            y = int(line.split(",")[1])
            xmax, ymax = max(xmax, x), max(ymax, y)
            if not (x,y) in grid:
                grid[(x,y)] = '#'
        else:                            # blank line => all points read
            xaxis = xmax
            yaxis = ymax
