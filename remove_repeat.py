s=input("Enter a string:")
rew=""
for ch in s:
    if ch not in rew:
        rew+=ch
print rew
