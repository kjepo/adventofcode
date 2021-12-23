#!/usr/bin/env python3

import sys
import re

class Cube:
    def __init__(self, on, x0, x1, y0, y1, z0, z1):
        self.on = on
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

    def __str__(self):
        return ("+" if self.on else "-") \
            + "(" + str(self.x0) + "--" + str(self.x1) \
            + "," + str(self.y0) + "--" + str(self.y1) \
            + "," + str(self.z0) + "--" + str(self.z1) + ")"

    def __repr__(self):
        return self.__str__()

    # compute intersection with self and another cube c
    def intersect(self, c):
        ix0 = max(self.x0, c.x0);
        ix1 = min(self.x1, c.x1)
        iy0 = max(self.y0, c.y0);
        iy1 = min(self.y1, c.y1)
        iz0 = max(self.z0, c.z0);
        iz1 = min(self.z1, c.z1)
        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            return Cube(False, ix0, ix1, iy0, iy1, iz0, iz1)
        else:
            return None

    def volume(self):
        # Use 2D version for debugging on paper...
#        vol = (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1)
        vol = (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)
        return vol

def overlapbox(b, box, boxes):
    temp_box = box.intersect(b)
    if temp_box:
        return temp_box.volume() - overlap(temp_box, boxes[1 + boxes.index(b):])
    else:
        return 0

def overlap(box, boxes):
    m = map(lambda b: overlapbox(b, box, boxes), boxes)
    return sum(m)

if __name__ == "__main__":
    cubes = []
    with open(sys.argv[1]) as f:
        # read instructions
        for line in f.read().splitlines():
            if line:
                [x1, x2, y1, y2, z1, z2] = map(int, re.findall(r'[-]?\d+', line))
                c = Cube(line[1] == "n", x1, x2, y1, y2, z1, z2)
                cubes.append(c)
        # look at all instructions in reverse (start with the last)
        # the last instruction will leave all its cells on.
        # the 2nd last instruction must look at the intersection with the last instruction
        # the 3rd last instruction must look at the intersection with the last two instructions
        # etc
        cubes.reverse()
        boxes = [ ]
        on_counter = 0
        for c in cubes:
            print(c)
            if c.on:
                on_counter += c.volume() - overlap(c, boxes)
            boxes.append(c)
        print(on_counter)
