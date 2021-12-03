#!/usr/bin/env python3

import sys

def oxygen(b, list):
    if len(list) < 2:
        return int(''.join(list), 2)
    zeros = [x for x in list if x[b]=='0']
    ones  = [x for x in list if x[b]=='1']
    if len(zeros) > len(ones):
        return oxygen(b+1, zeros)
    else:
        return oxygen(b+1, ones)

def scrubber(b, list):
    if len(list) < 2:
        return int(''.join(list), 2)
    zeros = [x for x in list if x[b]=='0']
    ones  = [x for x in list if x[b]=='1']
    if len(zeros) <= len(ones):
        return scrubber(b+1, zeros)
    else:
        return scrubber(b+1, ones)

if __name__ == "__main__":
    list = open(sys.argv[1]).read().split()
    print(oxygen(0, list) * scrubber(0, list))
