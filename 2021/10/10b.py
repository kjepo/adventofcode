#!/usr/bin/env python3

# Grammar
# E --> T E | epsilon
# T --> [ E ]   |  ( E )  |  < E >  | ( E ) |  epsilon

import sys

score = 0
completion_score = { ')': 1, ']': 2, '}': 3, '>': 4 }

# simple scanner: sets c to next character or "#" if we've reached end of line
def scan(): 
    global line, c
    if len(line) == 0:
        c = "#"
    else:
        c = line[0]
        if c in "{([<>])}":
            line = line[1:]
        else:
            c = "#"

def E():
    if c == "#":
        return
    if c in "[{<(":
        T()
        E()

def T():
    global line, score
    closing = { "{": "}", "(": ")", "[": "]", "<": ">" }
    opening = c
    scan()
    E()
    if c == closing[opening]:
        scan()
    else:
        # print("Syntax error: ", c, "expected", closing[opening])
        if c == "#" and score >= 0: # auto-complete
            score = score*5 + completion_score[closing[opening]]
        else:                # syntax error: don't calculate auto-complete score
            score = -1
            line = []

totalscores = []
lines = open(sys.argv[1]).readlines()
for line in lines:
    line = line.strip()
    # print(line)
    scan()
    E()
    if score > 0:
        totalscores.append(score)
    score = 0
totalscores.sort()
# print(totalscores)
print(totalscores[int(len(totalscores)/2)])
