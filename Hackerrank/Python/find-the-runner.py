# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
x = []
n=input()
a=raw_input()
ll=[]
ll=map(int,a.split())
lll=len(ll)
if lll==n:
   a=max(ll)
   ll.remove(max(ll))
   while a==max(ll):
      ll.remove(max(ll))
   print max(ll)



