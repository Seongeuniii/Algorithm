import sys,math
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):
  cost = [math.inf]*(N+1)
  cost[start] = 0
  heap = []
  heappush(heap, (0,start))

  while heap:
    value, node = heappop(heap)
    if cost[node] < value:
      continue
    for nd, v in graph[node]:
      if cost[nd] > value + v:
        cost[nd] = value + v
        heappush(heap, (value+v,nd))
        answer[nd][start] = node

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
answer = [['-']*(N+1) for _ in range(N+1)]

for _ in range(M):
  a,b,v = map(int,input().split())
  graph[a].append((b,v))
  graph[b].append((a,v))

for n in range(N+1):
  dijkstra(n)

for i in range(1,N+1):
  print(' '.join(map(str,answer[i][1:])))