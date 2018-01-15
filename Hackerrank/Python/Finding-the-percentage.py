# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
dic={}
lis=[]
for i in range(n):
    a=raw_input()
    lis=a.split()
    d=lis[0]
    lis.remove(lis[0])
    lst1=list(map(float,lis))
    dic[d]=lst1
name=raw_input()
if name in dic:
    marks=dic[name]
t=0
for i in marks:
    t=t+i
t=t/len(marks)
print "%.2f" %t



