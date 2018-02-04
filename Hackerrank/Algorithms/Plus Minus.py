#----------> PYTHON 3 <----------
import sys

def plusMinus(arr):
    length=len(arr)
    zeros=0
    positive=0
    negative=0
    # Complete this function
    for i in arr:
        if i==0:
            zeros=zeros+1
        elif i>=0:
            positive=positive+1
        else:
            negative=negative+1
    
    print(round(positive/length,5))
    print(round(negative/length,5))
    print(round(zeros/length,5))
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)

