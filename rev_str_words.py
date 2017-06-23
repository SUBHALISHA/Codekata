s=input("Enter a line")
list=[]
list=s.split()
l=len(list)
list2=[]
for j in range(l-1,-1,-1):
    list2.append(list[j])
print list2
