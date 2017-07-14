list=[]
ans=[]
n=input("Enter number of elements in list")
count=0
for i in range(n):
  list.append(input())
  ans.append(0)
for i in range(n):
  a=list[i]
  for j in range(i+1,n):
    if(list[j]==a):
      ans[i]+=1
      ans[j]+=1
for i in range(0,n):
  if(ans[i]==0):
    print ("The unique element is "+str(list[i]))
