s=input("Enter input in format int /or% int:")
l=len(s)
list1=[]
list1=s.split()
op1=int(list1[0])
op=list1[1]
op2=int(list1[2])
if(op=='%'):
    ans= op1 % op2
else:
    ans=op1/op2
print str(s)+"="+str(ans)
