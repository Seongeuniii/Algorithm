import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(s):
  
  for k in range(N+1):
    for i in range(N+1):
      for j in range(N+1):
        if d[i][k] + d[k][j] < d[i][j]:
          d[i][j] = d[i][k] + d[k][j]
  
  for i in range(1, N+1):
    for j in range(1, N+1):
      if d[i][j] +  d[j][i] < 0:
        return 'YES'

  return 'NO'

for _ in range(int(input())):
  N, M, W = map(int, input().split())
  d = [[math.inf]*(N+1) for _ in range(N+1)]

  for i in range(1, N+1):
    d[i][i] = 0

  for _ in range(M):
    S, E, T = map(int, input().split())
    d[S][E] = T
    d[E][S] = T

  for _ in range(W):
    S, E, T = map(int, input().split())
    d[S][E] = -T

  print(dijkstra(1))