#!/usr/bin/env python3

import sys
rule = { } # e.g. rule["NN"] = "C"

def expand():
    new = ""
    # slide 2 character window over polymer, apply rule to window
    for i in range(len(polymer) - 1):
        segment = polymer[i:i+2]
        new = new + polymer[i] + rule[segment][0:2]
    new = new + polymer[-1]
    return new

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        polymer = lines[0].strip()
        for line in lines[1:]:
            if "->" in line:
                left, right = line.split(" -> ")
                rule[left] = right
        for _ in range(10):
            polymer = expand()
            
        freq = { }
        for c in polymer:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        mc = max(zip(freq.values(), freq.keys()))[1]
        lc = min(zip(freq.values(), freq.keys()))[1]
        print(lc, freq[lc], mc, freq[mc], "=>", freq[mc] - freq[lc])
    
