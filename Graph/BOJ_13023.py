#DFS
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start,cnt):
  if cnt == 5:
    print(1)
    sys.exit()
  for nd in graph[start]:
    if not visited[nd]:
      visited[nd] = 1
      dfs(nd,cnt+1)
      visited[nd] = 0

for i in range(N):
  visited = [0]*N
  visited[i] = 1
  dfs(i,1)
print(0)

#BFS
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  q = deque()
  q.append((start,[start]))
  while q:
    node, relation = q.popleft()
    for nd in graph[node]:
      if nd not in relation:
        if len(relation) == 4:
          print(1)
          sys.exit()
        else:
          li = relation + [nd]
          q.append((nd,li))

for i in range(N):
  bfs(i)
print(0)