# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
l=[]
l=map(int,raw_input().split())
sum=0
for i in range(n):
   sum=sum+l[i]
print sum