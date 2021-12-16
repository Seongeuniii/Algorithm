import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
  li = [0] + list(map(int,input().split()))
  for j in range(1,N+1):
    if i==j:
      continue
    if li[j]:
      graph[i].append(j)

plan = list(map(int,input().split()))
visited = [0]*(N+1)

def bfs(start):
  q = deque()
  visited[start] = 1
  q.append(start)
  while q:
    node = q.popleft()
    for nd in graph[node]:
      if not visited[nd]:
        visited[nd] = 1
        q.append(nd)

bfs(plan[0])

for p in plan:
  if not visited[p]:
    print('NO')
    sys.exit()

print('YES')