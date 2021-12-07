#!/usr/bin/env python3

data = list(map(int, open("data.txt").read().split(",")))

def cost(p):
    global data
    return sum([abs(d-p) for d in data])

print(min([cost(p) for p in range(min(data),max(data))]))
