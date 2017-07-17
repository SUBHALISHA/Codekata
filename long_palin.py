m=0
s=""
twmp=""
temp1=""
temp2=""
st=input("Enter String:")
l=len(st)
for i in range(l):
  for j in range(i+1,l):
    temp=st[i:j]
    temp1=temp
    temp=temp[::-1]
    if(temp1==temp and len(temp)>m):
      m=len(temp1)
      temp2=temp1
print temp2
