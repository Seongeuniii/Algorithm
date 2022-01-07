import sys
from collections import deque
input = sys.stdin.readline

N,K,M = map(int,input().split())
hypertube = [[] for _ in range(N+M+1)]

for m in range(N+1,N+M+1):
  for l in list(map(int,input().split())):
    hypertube[l].append(m)
    hypertube[m].append(l)

def bfs(start):
  check = [-1]*(N+M+1)
  q = deque()
  q.append((start,1))
  check[start] = 1
  
  while q:
    node, cnt = q.popleft()
    for nd in hypertube[node]:
      if check[nd] != -1:
          continue
      if nd <= N:
        q.append((nd,cnt+1))
      else:
        q.append((nd,cnt))
      check[nd] = cnt+1

  return check[N]

print(bfs(1))