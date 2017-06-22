sum=0
n=input("Enter n:")
if(n<0):
  print ("Enter positive integer")
else:
  for i in range(1,n):
    sum=sum+i
  print sum
