#!/usr/bin/env python3

import sys
from functools import lru_cache

TOPSCORE = 21

# return new position and score for player at position p and score s when rolling n
def roll(p, s, n):
    pn = p + n
    while pn > 10:
        pn -= 10
    sn = s + pn
    return (pn, sn)

# player1 -- returns <c1, c2> where
# c1 is number of universes where player 1 wins
# c2 is number of universes where player 2 wins
# Python has a cache to store previous function values
# If your language doesn't have it, you can use an
# associative array MEMO[pos1,pos2,score1,score2]

@lru_cache(40000)
def player1(pos1, pos2, score1, score2):
    global UC
    if score2 >= TOPSCORE:
        return (0, 1)
    wins1, wins2 = 0, 0
    for r1 in [1,2,3]:
        for r2 in [1,2,3]:
            for r3 in [1,2,3]:
                (p1, s1) = roll(pos1, score1, r1+r2+r3)
                (c1, c2) = player2(p1, pos2, s1, score2)
                wins1, wins2 = wins1 + c2, wins2 + c1
    return (wins1, wins2)

# player2 -- roles reversed
@lru_cache(40000)
def player2(pos2, pos1, score2, score1):
    global UC
    if score2 >= TOPSCORE:
        return (0, 1)
    wins1, wins2 = 0, 0
    for r1 in [1,2,3]:
        for r2 in [1,2,3]:
            for r3 in [1,2,3]:
                (p2, s2) = roll(pos1, score1, r1+r2+r3)
                (c1, c2) = player1(pos2, p2, score2, s2)
                wins1, wins2 = wins1 + c2, wins2 + c1
    return (wins1, wins2)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        pos1, pos2 = int(lines[0][-1]), int(lines[1][-1])
        c = player1(pos1, pos2, 0, 0)
        print("player 1:", c[0], "wins")
        print("player 2:", c[1], "wins")
        if c[0] > c[1]:
            print("player 1 wins more often")
        else:
            print("player 2 wins more often")
