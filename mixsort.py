n=input("Enter number of elements to be sorted:")
list=[]
for i in range(n):
    list.append(input("Enter "+str(i)+" :"))
for i in range(n):
    j=0
    while j<n-1:
        if(list[i]>list[j]):
            t=list[j]
            list[j]=list[i]
            list[i]=t
        j=j+1
print list
mid=n/2
i=0
while(i<mid):
    while(j>mid-1):
        print list[i]
        print list[j]
        i+=1
        j-=1
