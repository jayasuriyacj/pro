inp1 = int(input())
inp2 = list(map(int,input().split()))
inp3 = []
for i in inp2:
  inp4 = bin(i)
  inp3.append(inp4)
inp5 = sorted(inp3)
inp5.reverse()
for i in inp5:
  print(int(i,2))
