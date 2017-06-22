    string1=input("Enter string:")
    string2=""
    i=0
    l=len(string1)
    while(i<l):
        if(string1[i]==" "):
            a=string1[i+1].upper()
            string2+=a
            i=i+2
        else:
            string2+=string1[i]
            i=i+1
    print string2
