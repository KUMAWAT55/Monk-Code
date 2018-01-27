##############################
N=int(input())
for i in range(N):
  s1,s2=input().split()
  if(''.join(sorted(s1))==''.join(sorted(s2))):
    print ("YES")
  else:
    print ("NO")
