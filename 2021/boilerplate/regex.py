#!/usr/bin/env python3

# parses input like this into array of numbers
#
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# etc
#
# change [a,b,c,d] to, e.g., [a,b] if you know there are
# only two numbers per line. Numbers can be negative and
# surrounded by all kinds of crap, i.e., this also works
#
# 0 9 -- 5 9
# 8 0 -- 0 8
# 9 4 -- 3 4
# etc

import sys
import re

def solve(a,b,c,d):
    print(a,b,c,d)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f.read().splitlines():
            if line:
                [a,b,c,d] = map(int, re.findall(r'[-]?\d+', line))
                solve(a,b,c,d)
