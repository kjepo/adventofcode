#!/usr/bin/env python3

# We can't store all the timers in one long list because it grows too big
# Instead, store how _many_ timers there are of a value t, t = 0..8

days = 256
state = list(map(int, open("data.txt").read().split(",")))
ntimers = 9*[0]                   # ntimers[i] = nr of timers with value i
for n in state:
    ntimers[n] += 1
for _ in range(days):
    t = ntimers[0]                # these are about to create new fish
    for i in range(0,8):
        ntimers[i] = ntimers[i+1] # decrement timers 
    ntimers[8] = t                # new-borns
    ntimers[6] += t               # parent starts at 6 again
print(sum(ntimers))               # should be 1644874076764 for the above state
