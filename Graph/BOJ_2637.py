import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
indeg = [0]*(N+1)

for _ in range(M):
  X,Y,K = map(int,input().split()) # X를 만드는데 Y가 k개 필요
  graph[X].append([Y,K])
  indeg[Y] += 1

answer = [0]*(N+1)
dp = [0]*(N+1)

def bfs(toy_num):
  q = deque()
  q.append(toy_num)
  dp[toy_num] = 1
  while q:
    tn = q.popleft()
    if not graph[tn]:
      answer[tn] += dp[tn]
      continue
    for nd,cnt in graph[tn]:
      indeg[nd] -= 1
      dp[nd] += (dp[tn]*cnt)
      if indeg[nd] == 0:
        q.append(nd)
  
bfs(N)
for i in range(1,N):
  if answer[i]:
    print(i, answer[i])