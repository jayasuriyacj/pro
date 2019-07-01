inp1,inp2=list(map(int,input().split()))
i1=list(map(int,input().split()))[:inp1]
j1=list(map(int,input().split()))[:inp2]
j2=list(map(int,input().split()))[:inp2]
j3=list(map(int,input().split()))[:inp2]
print(min(i1+j1))
print(min(i1+j2))
print(min(i1+j3))
