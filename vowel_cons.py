
s=input("Enter String:")
print "given string:"+s
l=['a','e','i','o','u','A','E','I','O','U']
v=[]
cons=[]
for i in s:
    if i in l:
        v.append(i)
    else:
        cons.append(i)
if len(v)==0:
    print "No vowels"
else:
    print "The vowels are:"
    print v
if len(cons)==0:
    print "No consonants"
else:
    print "The consonants are:"
    print cons
