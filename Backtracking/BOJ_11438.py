import sys
from collections import deque
input = sys.stdin.readline

def bfs(root):
  q = deque([(root, 0)])
  c[root] = 1

  while q:
    node, depth  = q.popleft()
    d[node] = depth
    for nd in graph[node]:
      if not c[nd]:
        c[nd] = 1
        parent[nd][0] = node
        q.append((nd, depth+1))

def set_parent(root):
  bfs(root)
  for i in range(1, max_depth):
    for j in range(1, N+1):
      parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
  if d[a] > d[b]:
    a, b = b, a
  
  for i in range(max_depth-1, -1, -1):
    if d[b] - d[a] >= (1 << i):
      b = parent[b][i]

  if a == b:
    return a

  for i in range(max_depth-1, -1, -1):
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]

  return parent[a][0]

N = int(input())
max_depth = 17
graph = [[] for _ in range(N+1)]
parent = [[0] * max_depth for _ in range(N+1)]
d = [0]*(N+1)
c = [0]*(N+1)

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

set_parent(1)

for _ in range(int(input())):
  f1, f2 = map(int, input().split())
  print(lca(f1, f2))