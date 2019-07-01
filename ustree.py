inp1,inp2=map(int,input().split())
inp3=list(map(int,input().split()))
inp1=[]
inp3.insert(0,0)
for j in range(inp2):
     v=[]
     s1=0
     k,l=map(int,input().split())
     for i in range(k,l+1):         
         s1^=inp3[i]     
     inp1.append(s1)
for j in inp1:
    print(j)
