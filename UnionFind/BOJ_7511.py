import sys
input = sys.stdin.readline

def find(x):
  if x == parent[x]:
    return x
  else:
    y = find(parent[x])
    parent[x] = y
    return y

def union(x,y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for t in range(1,int(input())+1):
  n = int(input()) 
  k = int(input())
  parent= [p for p in range(n+1)]

  for _ in range(k):
    a,b = map(int,input().split())
    union(a,b)

  print('Scenario', t, end='')
  print(':')
  for _ in range(int(input())):
    u,v = map(int,input().split())
    if find(parent[u]) == find(parent[v]):
      print(1)
    else:
      print(0)
  print()