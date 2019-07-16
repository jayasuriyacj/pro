inp1=input()
inp2=input()
inp3=[]
inp4=[]
inp5=[]
for i in inp1:
    inp3.append(ord(i)-ord('a'))
for i in inp2:
    inp4.append(ord(i)-ord('a'))
for i,j in zip(inp3,inp4):
    inp5.append((chr((i+j)%26+ord('a')+1)))
print("".join(inp5))
