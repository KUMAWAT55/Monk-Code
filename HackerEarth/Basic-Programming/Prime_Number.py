    def isPrime(x):
        if x<2:
            return 0
        for i in range(2,x):
            if not x%i:
               return 0
        return 1
     
    n=int(input())
    l=[]
    for j in range(2,n):
      
      if isPrime(j)==1:
        l.append(j)
    print (' '.join(repr(e) for e in l))
