a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
AB = A-B
print(len(AB))
for l in sorted(list(AB)):
  print(l,end=' ')