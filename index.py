n=input("Enter the number of elements:")
list=[]
count=0
for i in range(n):
  list.append(input())
for i in range(n):
  for j in range(i+1,n):
    if(list[i]>list[j]):
      t=list[i]
      list[i]=list[j]
      list[j]=t
print list
for i in range(n):
  if(list[i]==i):
    print i
    count+=1
if(count==0):
  print "No such element"
