def gcd(x,y):
    if(x>y):
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
x=input("Enter x:")
y=input("Enter y:")
coprime=gcd(x,y)
if(coprime==1):
    print"Given numbers are coprime"
else:
    print "Given numbers are not coprime"
