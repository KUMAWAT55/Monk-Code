    n=int(raw_input())
    str=map(int,raw_input().split())
    ans=1
    import math
    if 1<=n<=1000 and 1<=len(str)<=1000:
        for i in range(len(str)):
            ans=(ans*str[i])%(10**9+7)
        print ans
