#!/usr/bin/env python3

data = list(map(int, open("data.txt").read().split(",")))

def fuel(n):     # 1+2+...+n = n(n+1)/2
    return int(n*(n+1)/2)

def cost(p):
    global data
    return sum([fuel(abs(d-p)) for d in data])

print(min([cost(p) for p in range(min(data),max(data))]))


