#!/usr/bin/env python3

import sys
import re

def solve(a,b,c,d):
    print("%d,%d -> %d,%d" % (a,b,c,d))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f.read().splitlines():
            [a,b,c,d] = map(int, re.findall(r'[-]?\d+', line))
            solve(a,b,c,d)
