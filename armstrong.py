n=input("Enter number:")
val=n
sum=0
while(n>0):
  q=n/10
  r=n%10
  sum=sum+(r*r*r)
  n=q
if(sum==val):
  print(str(val)+" is a armstrong number")
else:
  print(str(val)+" is not a armstrong number")
