import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# root부터 depth 계산
def dfs(x, depth):
  c[x] = 1
  d[x] = depth
  for nd in graph[x]:
    if c[nd]:
      continue
    parent[nd][0] = x
    dfs(nd, depth+1)

# 전체 부모 관계 설정하는 함수
def set_parent(root):
  dfs(root, 0) # 루트노드: 1 루트깊이: 0 => 기준으로 전체 노드들의 깊이 계산
  for i in range(1, max_depth): # (2**1부터 2**20까지)
    for j in range(1, N+1): # 루트부터 전체
      parent[j][i] = parent[parent[j][i-1]][i-1]

# 최소 공통 조상을 찾는 함수
def lca(a, b):
  # b가 더 깊도록 설정
  if d[a] > d[b]:
    a, b = b, a
  
  # depth가 같아지도록
  for i in range(max_depth-1, -1, -1):
    if d[b] - d[a] >= (1 << i):
      b = parent[b][i]

  # 공통 조상이 a
  if a == b:
    return a

  # 같은 depth상에서 조상을 향해 거슬러 올라가기
  for i in range(max_depth-1, -1, -1):
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]

  # 이후에 부모가 찾고자 하는 조상
  return parent[a][0]

N = int(input())
max_depth = 17
graph = [[] for _ in range(N+1)]
parent = [[0] * max_depth for _ in range(N+1)]
d = [0]*(N+1)
c = [0]*(N+1)

for _ in range(N-1):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

set_parent(1)

for _ in range(int(input())):
  f1, f2 = map(int, input().split())
  print(lca(f1, f2))