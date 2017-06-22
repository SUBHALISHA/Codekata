st=input("Enter a line:")
l=len(st)
count=0
for i in range(l):
    if st[i].isalpha():
        count+=1
print "The  number of characters in '"+st+"' is "+str(count)
