inp1=int(input())
inp2=list(map(int,input().split()))
inp3=[1]*inp1
for i in range(inp1):
    if i==0:
        if inp2[i]>inp2[i+1]:
            inp3[i]=inp3[i]+inp3[i+1]
    elif i>0:
        if inp2[i]>inp2[i-1]:
            inp3[i]=inp3[i]+inp3[i-1]
print(sum(inp3))
