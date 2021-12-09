#!/usr/bin/env python3

# "1", "4", "7", "8" are unique in that only "1" uses 2 segments, only "4" uses 4 segments, etc
# In other words, if 7 segments light up, it is trying to show an "8"
# 1 uses cf
# 4 uses bcdf
# 7 uses acf
# 8 uses abcdefg

data = open("data.txt").readlines()
count = 0
for d in data:
    values = d.split("|")[1].strip().split(" ")
    for v in values:
        if len(v) in [2,4,3,7]:
            #print(v)
            count += 1
print(count)
