st=input("Enter a line:")
l=len(st)
count=0
for i in range(l):
    if st[i].isalnum():
        count+=1
ans=l-count
print("Number of special characters in "+st+" is "+str(ans))
