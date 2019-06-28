ins1,ins2=input().split()
del1=abs(len(ins1)-len(ins2))
for j in range(len(ins1)):
    if len(ins2)==1 and ins2[j] in ins1:
        break
    if ins1[j]!=ins2[j]:
        del1+=1
print(del1)
