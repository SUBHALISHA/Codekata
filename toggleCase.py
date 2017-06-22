s=input("Enter a string:")
rew=""
for ch in s:
    if ch.isupper():
        rew+=ch.lower()
    else:
        rew+=ch.upper()
print rew
