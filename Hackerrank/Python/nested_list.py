l=[]
for _ in range(0,int(input())):
    l.append([input(), float(input())])
s_h=sorted(list(set([marks for name,marks in l])))[1]
for a,b in sorted(l):
  if b==s_h:
    print(a)
