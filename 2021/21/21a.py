#!/usr/bin/env python3

import sys
import re

die = 1                         # die starts at 1 and goes to 100
rolls = 0                       # number of rolls

def roll():
    global die, rolls
    n = die
    die += 1
    rolls += 1
    if die > 100:
        die = 1
    return n

def roll3():
    return roll() + roll() + roll()

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        pos1, pos2 = int(lines[0][-1]), int(lines[1][-1])
        score1, score2 = 0, 0
        while True:
            print("Player 1 rolls %d+%d+%d" % (die, die+1, die+2), end=" ")
            pos1 += roll3()
            while pos1 > 10:
                pos1 -= 10
            score1 += pos1
            print("and moves to space %d for a total score of %d." % (pos1, score1))
            if score1 >= 1000:
                break
            print("Player 2 rolls %d+%d+%d" % (die, die+1, die+2), end=" ")
            pos2 += roll3()
            while pos2 > 10:
                pos2 -= 10
            score2 += pos2
            print("and moves to space %d for a total score of %d." % (pos2, score2))
            if score2 >= 1000:
                break
        print("-->", min(score1, score2) * rolls)
