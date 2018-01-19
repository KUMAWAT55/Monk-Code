n=int(input())
arr=set(map(int,input().split()))
def average(arr):
    sum=0
    # your code goes here
    for i in arr:
        sum=sum+i
    return sum/len(arr)
print(average(arr))
