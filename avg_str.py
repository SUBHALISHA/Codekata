s=input("Enter a string:")
l=len(s)
sum=0
for i in range(l):
    sum=sum+ord(s[i])
ans=sum/l
print chr(ans)
