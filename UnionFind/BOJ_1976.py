import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parent= [p for p in range(N+1)]

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

for i in range(1,N+1):
  li = [0] + list(map(int,input().split()))
  for j in range(1,N+1):
    if li[j]:
      union(i,j)

plan = list(map(int,input().split()))

for t in range(M):
  if parent[plan[t]] != parent[plan[0]]:
    print('NO')
    sys.exit()
print('YES')
