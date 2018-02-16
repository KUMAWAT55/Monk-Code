    n=raw_input()
    if 1<=len(n)<=100:
        c=''.join(reversed(n))
        if n==c:
           print "YES"
        else:
           print "NO"
