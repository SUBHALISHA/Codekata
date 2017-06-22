st=input("Enter a line:")
st=st.lstrip()
st=st.rstrip()
l=len(st)
count=1
for i in range(l):
    if st[i].isspace():
        count+=1
print "The  number of words in '"+st+"' is "+str(count
