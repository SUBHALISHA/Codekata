st=input("Enter string:")
le=len(st)
ans=""
rev=st[::-1]
l=['a','e','i','o','u','A','E','I','O','U']
for i in range(le):
    if rev[i] not in l:
        ans+=rev[i]
print "Given String: "+st
print ans
