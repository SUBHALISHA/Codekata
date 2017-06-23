print ("Enter 25 elements")
list=[]
for i in range(25):
    list.append(input("Enter element "+str(i+1)))
print list
for i in range(0,25):
    for j in range(i,24):
        if(list[i]>list[j]):
            t=list[j]
            list[j]=list[i]
            list[i]=t
print "The maximum number in list is:"+str(list[24])
