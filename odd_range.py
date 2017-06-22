i=0
st=input("Enter starting limit:")
dt=input("Enter ending limit:")
if(st%2!=0):
  i=1
  j=st
else:
  i=-1
  j=st+1
if(i==1):
  print("The odd numbers are:")
  while j<=dt:
    print(j)
    j=j+2
else:
    print("The odd numbers are:")
    while j<=dt:
      print(j)
      j=j+2
