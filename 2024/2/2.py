#!/usr/bin/env python3

import sys

def safe1(nums):
    diffs = []
    for i in range(1, len(nums)):
        diffs.append(nums[i]-nums[i-1])
    downs = list(filter(lambda x : x < 0 and x >= -3, diffs))
    ups = list(filter(lambda x : x > 0 and x <= 3, diffs))
    if len(downs) == len(diffs):
        return 1
    if len(ups) == len(diffs):
        return 1
    return 0

def safe2(nums):
    for i in range(len(nums)):
        if safe1(nums[:i] + nums[i+1:]):
            return 1
    return 0

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    safe_count_1 = safe_count_2 = 0
    for line in lines:
        nums = list(map(int, line.split()))
        safe_count_1 += safe1(nums)
        safe_count_2 += safe2(nums)
    print("Safe count for part 1:", safe_count_1)
    print("Safe count for part 2:", safe_count_2)
