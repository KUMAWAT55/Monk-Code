n=input()
a=raw_input()
n1=input()
b=raw_input()
lis=a.split()
newlis=list(map(int,lis))
myset=set(newlis)
lis1=b.split()
newlis1=list(map(int,lis1))
myset1=set(newlis1)
r=list(map(int,myset-myset1))
s=list(map(int,myset1-myset))
diff=sorted(r+s)
for i in range(len(diff)):
    print diff[i]
