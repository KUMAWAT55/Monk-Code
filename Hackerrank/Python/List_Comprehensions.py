# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
y=input()
z=input()
n=input()
print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c!=n])
