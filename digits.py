count=0
n=input("Enter n:")
val=n
if(n<0):
  n=-1*n
while(n>0):
  q=n/10
  r=n%10
  n=q
  count=count+1
print("There are "+str(count)+" digits in "+str(val))
