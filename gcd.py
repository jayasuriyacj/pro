import math
inp1,inp2=map(int,input().split())
a1=[]
b1=list(map(int,input().split()))
for i in range(0,inp2):
    a,b=map(int,input().split())
    a1.append([a,b])
for i in a1:
    c=i[0]-1
    d=i[1]-1
    print(math.gcd(b1[c],b1[d]))
