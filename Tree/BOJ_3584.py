import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, d): # root, depth
  depth[x] = d
  for nd in tree[x]:
    parent[nd] = x
    dfs(nd, d+1)

def lca(a, b):
  # depth가 같아지도록
  while depth[a] != depth[b]:
    if depth[a] > depth[b]:
      a = parent[a]
    else:
      b = parent[b]

  # 조상이 같아지도록
  while a != b:
    a = parent[a]
    b = parent[b]
  
  return a

for _ in range(int(input())):
  N = int(input())
  tree = [[] for _ in range(N+1)]
  parent = [0]*(N+1)
  depth = [0]*(N+1)
  p = [0]*(N+1)

  for _ in range(N-1):
    A, B = map(int, input().split())
    p[B] += 1
    tree[A].append(B)

  for i in range(1, N+1):
    if not p[i]:
      dfs(i, 0)
      break

  n1, n2 = map(int, input().split())
  print(lca(n1, n2))