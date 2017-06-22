s=input("Enter a string:")
st=s
alphabet="abcdefghijklmnopqrstuvwxyz"
s=s.lower()
rew=""
count=0
for ch in s:
    for l in alphabet:
        if ch==l and ch not in rew:
            rew+=ch
for ch in alphabet:
    for l in rew:
        if l==ch:
            count+=1
if(count==26):
    print(st+" is a pangram")
else:
    print(st+" is not a pangram")
