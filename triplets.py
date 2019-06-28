x1=int(input())
x2=list(map(int,input().split()))
a1=0
for x in range(len(x2)-2):
    for y in range(x+1,len(x2)-1):
        for z in range(y+1,len(x2)):
            if x2[x]<x2[y]<x2[z] and x<y<z:
                a1=a1+1
print(a1)
