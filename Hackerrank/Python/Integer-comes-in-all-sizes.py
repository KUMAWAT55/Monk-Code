# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
d=int(raw_input())
if 1<=a<=1000:
    if 1<=b<=1000:
        if 1<=c<=1000:
            if 1<=d<=1000:
                print pow(a,b)+pow(c,d)
