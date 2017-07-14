s=input("Enter string")
l=len(s)
al=0
dg=0
ans=0
for i in range(l):
  if(s[i].isalpha()):
    al=al+1
  if(s[i].isdigit()):
    dg=dg+1
ans=l-(al+dg)
print ans
