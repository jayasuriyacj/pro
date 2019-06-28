cj1,cj2=map(str,input().split())
a1=0
if len(cj2)>len(cj1):
  cj1,cj2=cj2,cj1
k=0
while k<len(cj2):
  a1+=(ord(cj1[k])-ord(cj2[k]))
  k+=1
for k in range(k,len(cj1)):
  a1+=ord(cj1[k])-ord('a')+1
print(a1)
