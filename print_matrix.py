n=input("Enter order of matrix")
list1=[[[] for i in range(n) ] for i in range(n)]
for i in range(n):
    for j in range(n):
        list1[i][j]=input("Enter elements in matrix " +str(i+1)+str(j+1))
print list1
'''for i in range(n):
    for j in range(n):
        print list1[i][j]'''
for i in range(n):
    if(i%2==0):
        j=0
        while j<n:
            print (list1[i][j]),
            j+=1
    else:
        k=n-1
        while(k>=0):
            print list1[i][k],
            k=k-1
