inp1=int(input())
inp2=[int(i) for i in input().split()]
inp3=0
for i in range(inp1):
   for j in range(i):
      if inp2[j]<inp2[i]:
         inp3+=inp2[j]
print(inp3)        
