inp1=int(input())
inp2=list(map(int,input().split()))
average=int(inp1/2)
x1=inp2[:average]
x2=inp2[average::]
if ((sum(x1)//len(x1))==(sum(x2)//len(x2))):
    print("yes")
else:
    print("no")
