#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
o = ""

for i in range(n-1, -1, -1):
    if i != 0:
        o += str(arr[i]) + " "
    else:
        o += str(arr[i])

print(o)
