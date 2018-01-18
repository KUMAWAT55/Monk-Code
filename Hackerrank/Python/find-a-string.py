count=0
string=input()
sub_string=input()
for i in range(len(string)):
  if(string[i:i+len(sub_string)]==sub_string):
    count+=1
     
print (count)

