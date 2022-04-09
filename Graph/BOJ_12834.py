import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
  cnt = [math.inf]*N
  dist = [math.inf]*N
  heap = []

  cnt[start] = 0
  dist[start] = 0
  heappush(heap, (0, 0, start))

  while heap:
    c, d, node = heappop(heap)

    if cnt[node] < c or (cnt[node] == c and dist[node] < d): continue

    for nd, v in enumerate(graph[node]):
      if v == 0: continue

      transfer = 0 if C[node] == C[nd] else 1

      if c + transfer < cnt[nd] or (c + transfer == cnt[nd] and d + v < dist[nd]):
        cnt[nd] = c + transfer
        dist[nd] = d + v
        heappush(heap, (cnt[nd], dist[nd], nd))
  
  print(cnt[M], dist[M])

N, M = map(int, input().split())
C = [int(input()) for _ in range(N)]
graph = [[0]*N for _ in range(N)]

for i in range(N):
  for j, e in enumerate(list(map(int, input().split()))):
    graph[i][j] = e

dijkstra(0)