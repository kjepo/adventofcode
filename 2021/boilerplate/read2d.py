#!/usr/bin/env python3

# creates a 2D array of int:s from input like this
#
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581

import sys
import numpy as np

def solve(map):
    xdim, ydim = map.shape
    print(xdim, ydim)
    print(map)

if __name__ == "__main__":
    map = np.genfromtxt(sys.argv[1], dtype=int, delimiter=1)
    solve(map)
