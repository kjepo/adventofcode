#!/usr/bin/env python3
import sys

# This is a simpler solution to 10A
# Turned out we didn't need a full-blown grammar with recursive descent parser
# Looking at the input strings, they are of the form
# [({(<(())[]>[[{[]{<()<>>
# After, e.g., "[", only "(", "{", "[", "<" or "]" can follow.
# In other words, ")", "}", ">" are not allowed
# Same reasoning for the other opening brackets "(", "<", "{"
# Therefore it suffices to keep a stack of open brackets and pop them off
# when we see the matching closing bracket.

closing = { '[' : ']', '(' : ')', '{' : '}', '<' : '>' }
value = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

def scan(line):
    stack = []
    for c in line:
        if c in "[({<":
            stack.append(c)
        elif c in "])}>" and closing[stack[-1]] == c:
            stack.pop()
        else: # syntax error, character c
            return value[c]
    return 0

score = 0
for line in open(sys.argv[1]).readlines():
    score += scan(line.strip())
print(score)
