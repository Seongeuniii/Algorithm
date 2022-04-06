import sys
input = sys.stdin.readline

def dfs(node):
  if node != 1 and len(tree[node]) == 1:
    return tree[node][0][1]
  
  d_sum = 0
  d = 0
  for nd, v in tree[node]:
    if not check[nd]:
      check[nd] = 1
      d_sum += dfs(nd)
    else:
      d = v

  if node == 1:
    return d_sum
  else:
    return min(d_sum, d)

for _ in range(int(input())):
  N, M = map(int, input().split())
  tree = [[] for _ in range(N+1)]
  check = [0]*(N+1)

  for _ in range(M):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))
  
  check[1] = 1
  print(dfs(1))