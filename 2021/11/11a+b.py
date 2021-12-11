#!/usr/bin/env python3
import sys

# This solution uses the same "trick" as day 8, namely
# Add a frame around the 2D array to simplify array indexing

# increment each octopus' energy level
def inc(A, y, x):
    A[y][x] += 1
    if A[y][x] == 10:
        inc(A, y-1, x-1); inc(A, y-1, x+0); inc(A, y-1, x+1); 
        inc(A, y-0, x-1);                   inc(A, y-0, x+1); 
        inc(A, y+1, x-1); inc(A, y+1, x+0); inc(A, y+1, x+1);

# each iteration step: increment energy levels, returns nr of flashes
def step(A):
    for y in range(1, ydim+1):
        for x in range(1, xdim+1):
            inc(A, y, x)
    flashes = 0
    for y in range(1, ydim+1):
        for x in range(1, xdim+1):
            if A[y][x] > 9:
                A[y][x] = 0
                flashes += 1
    return flashes

# if you need to pretty-print the energy levels
def pr(A):
    for y in range(1, ydim+1):
        for x in range(1, xdim+1):
            print(str(A[y][x]).rjust(2), end="")
        print()

# this needs to be _very_ negative so initial values don't become > 0 suddenly
MIN = -sys.maxsize
A = []
xdim = None

# read initial energy levels
if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    for line in lines:
        heights = [MIN] + [int(c) for c in line.strip()] + [MIN]
        if not xdim:
            xdim = len(heights) - 2
            A.append((xdim+2)*[MIN])
        A.append(heights)
    A.append((xdim+2)*[MIN])
ydim = len(A) - 2

# run simulation
total_flashes = 0
time = 0
while True:
    time += 1
    flashes = step(A)
    total_flashes += flashes
    if time == xdim*ydim:
        print("After", time, "steps there have been", total_flashes, "flashes")
    if flashes == 100:
        print("First step with all flashes", time)
        exit(0)
