l=map(int,raw_input().split())
if 1<=l[0]<=l[1]<=1000 and 1<=l[2]<=1000:
        if l[1]-l[0]==0:
            print 0
        else:
            print ((l[1]-l[0])/l[2])+1
