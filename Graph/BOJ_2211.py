import sys, math
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start):
  cost = [math.inf]*(N+1)
  parent = [0]*(N+1)
  heap = []

  cost[start] = 0
  heappush(heap,(0,start))

  while heap:
    value, node = heappop(heap)
    if cost[node] < value:
      continue
    for nd, v in graph[node]:
      if value + v < cost[nd]:
        cost[nd] = value + v
        parent[nd] = node
        heappush(heap, (value+v, nd))

  return parent

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

parent = dijkstra(1)
answer = []
for s in range(1,N+1):
  while parent[s]:
    answer.append((s, parent[s]))
    parent[s] = 0
    s = parent[s]
    
print(len(answer))
for a,b in answer:
  print(a,b)