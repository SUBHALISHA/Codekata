n=input("Enter number of elements in the series:")
f=0
s=1
print("The fibanocci series is")
print f
print s
for i in range (2,n):
    t=f+s
    f=s
    s=t
    print t
