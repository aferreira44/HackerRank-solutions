#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swaps = 0

for num in range(n-1,0,-1):
  for i in range(num):
    if a[i]>a[i+1]:
      temp = a[i]
      a[i] = a[i+1]
      a[i+1] = temp
      swaps = swaps + 1

print('Array is sorted in ' + str(swaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))