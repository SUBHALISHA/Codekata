def reduce(num, k):
  if(k<=0):
    return num
  if(num==0):
    return 10
  path1=reduce(num/10,k)*10+num%10
  path2=reduce(num/10,k-1)
  if(path1<path2):
    return path1
  else:
    return path2
n=input("Enter n:")
k=input("Enter k:")
ans=reduce(n,k)
print ans
