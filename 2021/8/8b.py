#!/usr/bin/env python3

# This is a pig sty.
#
# It works, but it's not pretty but I'm tired so f*ck it.
#
# Basically the program tries to figure out a mapping of signals to segments.
# 1, 7, 4, 8 are easy because the have a unique number of segments
# We can then figure out which one is 6 because it is the only display
# with 6 segments which doesn't have 1:s segments as a subset.
# That missing segment in 6 is either c or f so we can figure that out.
# The rest is just reasoning like this to get the map complete and apply it
# to the values.
#
# No-one is ever going to read this code anyway.

def subset(s1, s2):
    for c in s1:
        if not(c in s2):
            return False;
    return True;

def scan(token):
    global map, f, e
    if len(token) == 6 and (1 in map): # 0 6 9
        if not(subset(map[1], token)):            # 1 not subset of 6
            map[6] = token
        if (map[1][0] in token) and not(map[1][1] in token):
            c = map[1][1]
            f = map[1][0] # the segment that 1 and 6 has, but not 5
        if not(map[1][0] in token) and (map[1][1] in token):
            c = map[1][0]
            f = map[1][1] # the segment that 1 and 6 has, but not 5
        
    if len(token) == 6 and subset(map[1], token): # 0 or 9
        if (e and (e in token)):
            map[0] = token
        if (e and not(e in token)):
            map[9] = token

    if len(token) == 5 and f: # 2, 3, 5
        if (subset(map[1], token)):
            map[3] = token
        if not(f in token): # but f is not in 2
            map[2] = token
        if (f in token) and (6 in map) and (subset(token, map[6])):
            # 5 subset of 6 but 3 isn't
            map[5] = token
        if (f in token) and (6 in map) and not(subset(token, map[6])):
            map[3] = token
    if (5 in map) and (6 in map): # time to figure out e
        for segment in map[6]:
            if not(segment in map[5]):
                e = segment

def mainscan(token):
    global f, map
    i = 0
    while (not(0 in map and 1 in map and 2 in map and 3 in map and 4 in map and 5 in map and 6 in map and 7 in map and 8 in map and 9 in map)):
        if i > 20:
            break
        for token in tokens:
            token = [ c  for c in token ]
            token.sort()
            token = ''.join(token)
            scan(token)

data = open("data.txt").readlines()
count = 0
grandtotal = 0
for d in data:
    tokens = d.split("|")[0].strip().split(" ")
    values = d.split("|")[1].strip().split(" ")
    map = { }
    for token in tokens:
        for i in range(10):
            token = [ c  for c in token ]
            token.sort()
            token = ''.join(token)
            if len(token) == 2:
                map[1] = token
            if len(token) == 3:
                map[7] = token
            if len(token) == 4:
                map[4] = token
            if len(token) == 7:
                map[8] = token
    e = None
    f = None
    mainscan(token)

    sum = 0
    for value in values:
        value = [ c  for c in value ]
        value.sort()
        value = ''.join(value)
        digit = None
        for i in range(10):
            if (i in map) and (map[i] == value):
                digit = i
        sum = sum*10 + digit
    # print(sum)
    grandtotal += sum
print(grandtotal)

        
            

        
