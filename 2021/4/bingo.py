#!/usr/bin/env python3

import sys

def play(b, x):
    w = len(b[0])               # boards are always 5x5 though
    for i in range(w):
        for j in range(w):
            if b[i][j] == x:
                b[i][j] = -b[i][j]

def win(b):
    w = len(b[0])
    for i in range(w):
        winrow = True
        for j in range(w):
            if b[i][j] > 0:
                winrow = False
        if winrow:
            return True
    for j in range(w):
        wincolumn = True
        for i in range(w):
            if b[i][j] > 0:
                wincolumn = False
        if wincolumn:
            return True
    return False

def score(b):
    w = len(b[0])
    score = 0
    for i in range(w):
        for j in range(w):
            if b[i][j] > 0:
                score += b[i][j]
    return score

if __name__ == "__main__":
    file = open(sys.argv[1])
    numbers = list(map(int, file.readline().strip().split(",")))
    boards = []
    n = -1
    row = 0
    for line in file:
        line = line.strip()
        if line == "":          # create a new board
            n = n + 1
            boards.append([])
        else:                   # append row to current board
            boards[n].append(list(map(int,filter(None, line.split(" ")))))
    n = n + 1
    for x in numbers:
        for i in range(n):
            b = boards[i]
            play(b, x)
            if win(b):
                print(x * score(b))
                boards[i] = [[]]
