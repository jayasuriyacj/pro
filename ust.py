inp1,inp2=map(int,input().split())
inp3=list(map(int,input().split()))
for a in range (1,inp1):
    inp3[a]+=inp3[a-1]
for a in range (inp2):
    x,y=map(int,input().split())
    z=inp3[y-1] if x==1 else inp3[y-1]-inp3[x-2]
    print(z)
