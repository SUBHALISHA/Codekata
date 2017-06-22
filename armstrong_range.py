st=input("Enter starting limit:")
dt=input("Enter ending limit:")
count=0
for n in range(st,dt+1):
  val=n
  sum=0
  while(n>0):
    q=n/10
    r=n%10
    sum=sum+(r*r*r)
    n=q
  if(sum==val):
      print(val)
      count=count+1
if(count ==0):
  print("No armstrong numbers between the given limit")
