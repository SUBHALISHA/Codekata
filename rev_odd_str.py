s=input("Enter the long string")
s1=[]
ans=""
s1=s.split()
print s1
l=len(s1)
for i in range(l):
  if(i%2==0):
    st=s1[i]
    ans+=st[::-1]
    ans+=" "
  else:
    ans+=s1[i]
    ans+=" "
print ans
