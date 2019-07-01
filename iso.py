inp1,inp2=map(str,input().split())
if len(inp1)!=len(inp2):
  print("no")
a1=[inp1.count(ch) for ch in inp1]
b1=[inp2.count(ch) for ch in inp2]
if(a1==b1):
  print("yes")
else:
  print("no")
