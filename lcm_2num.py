x=input("Enter x:")
y=input("Enter y:")
if(x<y):
    larger=y
else:
    larger=x
while(True):
    if((larger%x==0) and (larger%y==0)):
        lcm=larger
        break
    larger=larger+1
print lcm
