import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
  N,K = map(int,input().split())
  time = [0] + list(map(int,input().split()))
  dp = [0]*(N+1)
  graph = [[] for _ in range(N+1)]
  indeg = [0]*(N+1)

  for _ in range(K):
    x,y = map(int,input().split())
    graph[x].append(y)
    indeg[y] += 1
  
  q = deque()
  for i in range(1, N+1):
    if not indeg[i]:
      dp[i] = time[i]
      q.append(i)

  while q:
    node = q.popleft()
    for nd in graph[node]:
      indeg[nd] -= 1
      dp[nd] = max(dp[nd], dp[node]+time[nd])
      if not indeg[nd]:
        q.append(nd)
  print(dp[int(input())])
