#!/usr/bin/env python3

days = 80
state = list(map(int, open("data.txt").read().split(",")))

for day in range(days):
    nextstate = []
    newfish = []
    for fish in state:
        fish = fish - 1
        if fish == -1:
            newfish.append(8)
            fish = 6
        nextstate.append(fish)
    state = nextstate
    for fish in newfish:
        nextstate.append(fish)
print(len(state))
