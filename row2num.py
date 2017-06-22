sum=0
rom= ['M', 'D', 'C', 'L', 'X', 'V', 'I']
num = [1000, 500, 100, 50,  10,  5,   1]
ans=[]
s=input("Enter a roman:")
l=len(s)
s=s.upper()
for i in s:
    if i not in rom:
        print("Enter valid numeral")
        exit()
for i in range(l):
    c=s[i]
    ind=num[rom.index(c)]
    try:
        nextvalue=num[rom.index(s[i+1])]
        if(nextvalue>ind):
            ind=-1*ind
    except IndexError:
        pass
    ans.append(ind)
for j in range(l):
    sum=sum+ans[j]
print sum
