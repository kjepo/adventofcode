#!/usr/bin/env python3

# Grammar
# E --> T E | epsilon
# T --> [ E ]   |  ( E )  |  < E >  | ( E ) |  epsilon

import sys

score = 0
errorscore = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
closing = { "{": "}", "(": ")", "[": "]", "<": ">" }

# simple scanner: sets c to next character or "#" if we've reached end of line
def scan(): 
    global line, c
    if len(line) == 0:
        c = "#"
    else:
        c = line[0]
        if c in "{([<>])}":
            line = line[1:]
        else:                   # if not valid character, line is corrupt... so EOL
            c = "#"

def E():
    if c == "#":
        return
    if c in "[{<(":
        T()
        E()

def T():
    global line, score
    opening = c
    scan()
    E()
    if c == closing[opening]:
        scan()
    else:
        # print("Syntax error: ", c, "expected", closing[opening])
        if c in errorscore:
            score += errorscore[c]
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
# print(totalscores)
print(sum(totalscores))
