list=[]
flag=-1
n=input("Enter number of elements in list")
for i in range(n):
  list.append(input())
for i in range(n):
  a=list[i]
  for j in range(i+1,n):
    if(list[j]==a):
      flag=1
      break
    else:
      continue
  if(flag==1):
    break
  else:
    continue
print ("The first repeated element is "+str(a))
