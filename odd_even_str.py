s=input("Enter a string:")
l=len(s)
r=""
i=0
while i<l:
    r+=s[i]
    i+=2
r+=" "
i=1
while i<l:
    r+=s[i]
    i+=2
print r
