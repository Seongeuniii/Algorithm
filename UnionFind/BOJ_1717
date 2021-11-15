import sys
input = sys.stdin.readline
N,M = map(int,input().split())
parent = [i for i in range(N+1)]

def find(x):
  if (x != parent[x]):
    parent[x] = find(parent[x])
  return parent[x]

def union(l,r):
  pl = find(l)
  pr = find(r)
  if pl != pr :
    parent[pr] = pl

for _ in range(M):
  a,b,c = map(int,input().split())
  if a == 0:
    union(b,c)
  else: 
    if find(b) == find(c):
      print('YES')
    else:
      print('NO')