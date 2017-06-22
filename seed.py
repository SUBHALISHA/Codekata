num=input("Enter a number:")
seed=input("Enter seed number:")
val=num
ans=1
while num>0:
    q=num/10
    rem=num%10
    num=q
    ans=rem*ans
ans=ans*val
if(ans==seed):
    print(str(seed)+" is a seed number of "+str(val))
else:
    print(str(seed)+" is not a seed number of "+str(val))
