def circle(r):
    area=3.14*r*r
    return area
def rect(l,b):
    area=l*b
    return area
def tri(l,b,h):
    area=(l*b*h)/2
    return area
ch=input("Enter\n 1.circle\n 2. Rectangle\n 3.Triangle")
if(ch==1):
    r=input("Enter radius:")
    ans=circle(r)
    print("Area is "+str(ans))
elif(ch==2):
    l=input("Enter length:")
    b=input("Enter breadth:")
    ans=rect(l,b)
    print("Area is "+str(ans))
elif(ch==3):
    l=input("Enter length:")
    b=input("Enter breadth:")
    h=input("Enter height:")
    ans=tri(l,b,h)
    print("Area is "+str(ans))
else:
    print("Sorry!!! No other option")
