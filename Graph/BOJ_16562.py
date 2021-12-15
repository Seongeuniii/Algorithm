import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
money = [0] + list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
check = [0]*(N+1)

for _ in range(M):
  v,w = map(int,input().split())
  graph[v].append(w)
  graph[w].append(v)

def bfs(start):
  q = deque()
  q.append(start)
  min_cost = money[start]
  while q:
    friend = q.popleft()
    for f in graph[friend]:
      if not check[f]:
        check[f] = 1
        min_cost = min(min_cost,money[f])
        q.append(f)
  return min_cost

answer = 0
for i in range(1,N+1):
  if not check[i]:
    check[i] = 1
    answer += bfs(i)
    
if answer <= K:
  print(answer)
else:
  print('Oh no')