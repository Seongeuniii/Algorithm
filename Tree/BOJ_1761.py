import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, depth, path):
  c[x] = 1
  d[x] = depth
  l[x] = path
  for nd, dp in graph[x]:
    if c[nd]:
      continue
    parent[nd][0] = x
    dfs(nd, depth + 1, path + dp)

def set_parent(root):
  dfs(root, 0, 0)
  for i in range(1, max_depth):
    for j in range(1, N+1):
      parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
  answer = 0

  if d[a] > d[b]:
    a, b = b, a

  for i in range(max_depth-1, -1, -1):
    if d[b] - d[a] >= (1 << i):
      answer += (l[b] - l[parent[b][i]])
      b = parent[b][i]

  if a == b:
    return answer

  for i in range(max_depth-1, -1, -1):
    if parent[a][i] != parent[b][i]:
      answer += ((l[b] - l[parent[b][i]]) + (l[a] - l[parent[a][i]]))
      a = parent[a][i] 
      b = parent[b][i]

  return answer + ((l[b] - l[parent[b][0]]) + (l[a] - l[parent[a][0]]))

N = int(input())
max_depth = 16
graph = [[] for _ in range(N+1)]
parent = [[0] * max_depth for _ in range(N+1)]
d = [0]*(N+1)
l = [0]*(N+1)
c = [0]*(N+1)

for _ in range(N-1):
  A, B, C = map(int, input().split())
  graph[A].append((B, C))
  graph[B].append((A, C))

set_parent(1)

for _ in range(int(input())):
  f1, f2 = map(int, input().split())
  print(lca(f1, f2))