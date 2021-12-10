#!/usr/bin/env python3
import sys

closing = { '[' : ']', '(' : ')', '{' : '}', '<' : '>' }
value = { '(': 1, '[': 2, '{': 3, '<': 4 }

def scan(line):
    stack = []
    for c in line:
        if c in "[({<":
            stack.append(c)
        elif c in "])}>" and closing[stack[-1]] == c:
            stack.pop()
        else: # syntax error, report no score
            return 0
    # for incomplete lines, add scores of closing characters
    score = 0
    while stack:
        c = stack.pop()
        score = score*5 + value[c]
    return score

scores = []
for line in open(sys.argv[1]).readlines():
    score = scan(line.strip())
    if score > 0:
        scores.append(score)
scores.sort()
print(scores[int(len(scores)/2)])
