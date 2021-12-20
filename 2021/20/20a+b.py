#!/usr/bin/env python3

# Usage: 20a.py alg-20.txt img-20.txt
#
# I've taken several shortcuts here due to lack of time (or interest?)
#
# 1. I've modified the image data file to use "1" instead of "#"
#    and "0" instead of "." so I can use numpy to read it.
#    The algorithm file still contains "#" and "." however.
# 2. I've embedded the image into a large 2D array so it can grow.
#    The size of this image is ad hoc: you need to increase the size until
#    the answer doesn't change.  A more clever way would be to let
#    the array grow as needed but I'm too lazy to implement this.
# 3. After each processing step, pixels around the border are lit.
#    This happens when the first character in the algorithm is "#", i.e., 
#    dark pixels in the padded area will result in a lit pixel.
#    Therefore, I set the border of the 2D array after each iteration
#    to whatever is further inside.
#
# PS Note that if the first character of the algorithm is "#", 3x3 dark pixels
#    will be lit in the next iteration.  And if the last character of the algorithm
#    is ".", 3x3 lit pixels will be dark in the next iteration. The example file
#    is more realistic but my algorithm file for the quiz had "#" first and "." last.

import numpy as np
import sys

# printing, if you need it
def P(a):
    N, M = a.shape
    assert(N == M)
    for y in range(N):
        for x in range(N):
            print("#" if a[y][x] == 1 else ".", end='')
        print()
    print()

# return bits for 3x3 pixel a[y][x] (as a string)
def read(a, y, x):
    N, M = a.shape
    assert(N == M)
    if y < 0 or y >= N:
        return "0"
    if x < 0 or x >= N:
        return "0"
    return str(a[y][x])

def process(A):
    N, _ = A.shape
    B = np.zeros((N,N), dtype=int)
    bits = ""
    for y in range(N):
        for x in range(N):
            n = read(A, y-1, x-1) + read(A, y-1, x) + read(A, y-1, x+1) \
              + read(A, y+0, x-1) + read(A, y+0, x) + read(A, y+0, x+1) \
              + read(A, y+1, x-1) + read(A, y+1, x) + read(A, y+1, x+1)
            B[y][x] = 1 if alg[int(n,2)] == "#" else 0
    for x in range(N):
        B[x][0] = B[1][1]
        B[x][N-1] = B[1][1]
        B[0][x] = B[1][1]
        B[N-1][x] = B[1][1]
    return B
    
PAD = 150    # use "large enough" to get correct answer (100 is too little)
if __name__ == "__main__":
    # read "algorithm" (table)
    with open(sys.argv[1]) as algfile:
        alg = ''.join([line.rstrip('\n') for line in algfile])
    # read image
    A = np.genfromtxt(sys.argv[2], dtype=int, delimiter=1)
    N, _ = A.shape
    # need to embed the image in a larger array because it grows
    DIM = N+PAD                 # dimension of larger array
    OFFSET = int((DIM - N)/2)   # offset for embedded array
    blank = np.zeros((DIM,DIM),dtype=int)
    # embed image into larger array
    blank[OFFSET:OFFSET+A.shape[0], OFFSET:OFFSET+A.shape[1]] = A
    # use larger array from now on, hope it's big enough
    A = blank
    for _ in range(50):
        A = process(A)
    print(np.count_nonzero(A>0))
