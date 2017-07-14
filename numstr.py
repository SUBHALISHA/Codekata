s=input("Enter string:")
l=len(s)
count=0
for i in range(0,l):
  if(s[i].isdigit()):
    count=count+1
print count
