#!/usr/bin/env python3
import sys
import re

repl_str = re.compile('^\d+$')

def hit(x0, y0):
    return x0 >= tx0 and x0 <= tx1 and y0 >= ty0 and y0 <= ty1

def fire(xv, yv):
    x0, y0 = 0,0
    ymax = -sys.maxsize
    # this termination condition works for problem set
    # but a general solution should consider the sign of ty0/ty1
    while x0 <= tx1 and y0 >= ty0: 
        x0, y0 = x0+xv, y0+yv
        # these are also simplifications of the rules:
        xv, yv = max(xv-1, 0), yv-1
        ymax = max(y0, ymax)
        if hit(x0, y0):
            return ymax
    return -sys.maxsize

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        for line in f.read().splitlines():
            [tx0,tx1,ty0,ty1] = map(int, re.findall(r'[-]?\d+', line))
            ymax = -sys.maxsize
            xvmax, yvmax = 0, 0
            hits = 0
            for xv in range(0, tx1+1):
                # 500 is a guess, increase until it doesn't change the answer
                for yv in range(min(ty0,ty1), 500): 
                    y = fire(xv, yv)
                    if y != -sys.maxsize:
                        hits += 1
                        if y > ymax:
                            ymax = y
                            xvmax, yvmax = xv, yv
            print("Part A: with initial speed (%d, %d) you reach a maximum altitude of %d" % (xvmax, yvmax, fire(xvmax, yvmax)))
            print("Part B: number of initial velocities that hit the target: %d" % hits)
