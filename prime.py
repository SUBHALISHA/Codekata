flag=0
st=input("Enter number:")
for x in range(2,st):
  if(st%x==0):
    flag=flag+1
if flag==0:
    print str(st)+" is a prime number"
else:
    print str(st)+" is not a prime number"
