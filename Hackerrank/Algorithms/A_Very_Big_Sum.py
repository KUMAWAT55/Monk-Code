#!/bin/python

import sys

sum=0
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for i in range(0,n):
    sum=sum+arr[i]
print sum
