list1=[]
ans=0
for i in range(0,10):
  list1.append(input("Enter number "+str(i+1)+":"))
for i in range(1,10):
  if(list1[i]>ans):
    ans=list1[i]
print ("The largest number is "+str(ans))
