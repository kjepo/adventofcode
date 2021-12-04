#!/usr/bin/env python3
# Advent of Code 2021, Day 4
# Run it with ./4a.py data.txt

import sys
import numpy as np

def winner(b):
    return np.any(np.all(b < 0, axis=0)) or np.any(np.all(b < 0, axis=1))

def sumpositives(b):
    return np.sum(np.clip(b, 0, sys.maxsize))

N = 5
numbers = np.loadtxt(sys.argv[1], max_rows=1, delimiter=',', dtype=int)
boards  = np.loadtxt(sys.argv[1], skiprows = 1, dtype=int)
nrboards = int(boards.size/(N*N))
boards = boards.reshape(nrboards,N,N)   # boards contain all N*N boards
for x in numbers:
    for b in boards:
        b[b==x] = -x            # if b contains x, set it to -x
        if winner(b):
            print(x*sumpositives(b))
            exit(0)
