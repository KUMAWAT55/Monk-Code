#!/bin/python3
#----------> PYTHON 3 <----------
import sys

def diagonalDifference(a,n):
    diagonal1=0
    diagonal2=0
    # Complete this function
    for i in range(n):
        diagonal1=a[i][i]+diagonal1
        diagonal2=a[i][n-1-i]+diagonal2
    return abs(diagonal1-diagonal2)
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a,n)
    print(result)

