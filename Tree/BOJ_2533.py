import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
  dp = [1, 0]
  for nd in tree[node]:
    if not check[nd]:
      check[nd] = 1
      result = dfs(nd)
      dp[0] += min(result)
      dp[1] += result[0]
  return dp

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
  u, v = map(int, input().split())
  tree[u].append(v)
  tree[v].append(u)

check = [0]*(N+1)
check[1] = 1
print(min(dfs(1)))