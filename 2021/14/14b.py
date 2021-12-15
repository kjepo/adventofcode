#!/usr/bin/env python3
from math import ceil
import sys

# store all rules, e.g., NN -> C is stored as rule["NN"] = "C"
rule = { } 

# c2 is a map so that, e.g., c2["NN"] = 3 if there are 3 occurrences of NN
c2 = { } 

def frequencies():
    global c2
    for i in range(len(polymer) - 1):
        segment = polymer[i:i+2]
        if segment not in c2:
            c2[segment] = 0
        c2[segment] += 1

def expand():
    global c2
    next = { }
    for f in c2:                # for each two-letter combination XY and a rule XY -> Z
        s1 = f[0] + rule[f]     # consider XZ
        s2 = rule[f] + f[1]     # consider ZY
        if not s1 in next:
            next[s1] = 0
        next[s1] += c2[f]     # increment counter for XZ
        if not s2 in next:
            next[s2] = 0
        next[s2] += c2[f]     # increment counter for ZY
    c2 = next

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        polymer = lines[0].strip()
        for line in lines[1:]:
            if "->" in line:
                left, right = line.split(" -> ")
                rule[left] = right
        frequencies()
        for _ in range(40):
            expand()
        freq = { }
        for f in c2:
            if f[0] not in freq:
                freq[f[0]] = 0
            freq[f[0]] += c2[f]
            if f[1] not in freq:
                freq[f[1]] = 0
            freq[f[1]] += c2[f]
        # each letter was counted twice, apart from 1st and last
        for f in freq:
            freq[f] = ceil(freq[f]/2)
        m = max(zip(freq.values(), freq.keys()))[1]
        l = min(zip(freq.values(), freq.keys()))[1]
        print(m, ":", freq[m],l, ":", freq[l], "=>", freq[m] - freq[l])

