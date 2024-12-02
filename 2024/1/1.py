#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    a1, a2 = [], []
    for line in lines:
        [x1, x2] = line.strip().split()
        a1.append(int(x1))
        a2.append(int(x2))
    a1.sort()
    a2.sort()
    dist = 0
    similarity = 0
    for i in range(len(a1)):
        dist += abs(a1[i] - a2[i])
        similarity += a1[i] * a2.count(a1[i])
    print("Solution to part one:", dist)
    print("Solution to part two:", similarity)
    
