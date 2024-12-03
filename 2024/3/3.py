#!/usr/bin/env python3

import sys, re

if __name__ == "__main__":
    data = open("input").read()
    sum1 = sum2 = 0
    on = 1
    for (a, b, do, dont) in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", data):
        if do:
            on = 1
        if dont:
            on = 0
        if a and b:
            sum1 += int(a)*int(b)
            sum2 += int(a)*int(b)*on
    print(sum1, sum2)
