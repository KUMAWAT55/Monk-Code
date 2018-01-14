# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
x = []
i = 0
n = int ( input())
for i in range (0,n):
   c=raw_input().split()
   if c[0] == 'insert':
      x.insert(int(c[1]),int(c[2]))
   if c[0] == 'print':
      print x
   elif c[0] == 'remove':
      x.remove(int(c[1]))
   elif c[0] == 'append':
      x.append(int(c[1]))
   elif c[0] == 'sort':
      x.sort()
   elif c[0] == 'pop':
      x.pop()
   elif c[0] == 'reverse':
      x.reverse()
