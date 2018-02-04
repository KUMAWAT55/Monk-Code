#----------> PYTHON 3 <----------
import sys

sum=0
n = int(input().strip())
arr = input().strip().split(' ')
for i in range(0,n):
    sum=sum+int(arr[i])
print (sum)
