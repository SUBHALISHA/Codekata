st=input("Enter a string:")
al=0
num=0
l=len(st)
print "The string is :"+st
for i in range(l):
    if(st[i].isalpha()):
        al=al+1
    if(st[i].isdigit()):
        num=num+1
an=al+num
print("The alphabets in the string are "+str(al))
print("The numbers in the string are "+str(num))
print("The alphanumeric characters in the string are "+str(an))
