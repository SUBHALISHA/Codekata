i=0
st=input("Enter starting limit:")
n=input("Enter  ending limit")
print "The prime numbers are:"
for i in range(st,n):
  if(i>1):
    for x in range(2,i):
      if(i%x==0):
        break
      else:
        print i
