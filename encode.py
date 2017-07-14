s1= input("Enter fiirst string:");
s2= input("Enter second string:");
l1= len(s1);
l2=len(s2);
ans1=""
ans2=""
for i in range(0,l1):
  ch=ord(s1[i])+10
  if(ch>122):
    a=ch-122
    ch=97+a-1
  ans1+=chr(ch)
ans2+=s2[0]
for i in range(1,l2-1):
  ch1=ord(s2[i])+10
  if(ch1>122):
    a1=ch1-122
    ch1=97+a1-1
  ans2+=chr(ch1)
ans2+=s2[l2-1]
print ans1
print ans2
