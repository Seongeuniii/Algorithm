import sys, math
from heapq import heappush, heappop
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
  a,b,c = map(int,input().split())
  graph[a].append((c,b))
  graph[b].append((c,a))
v1,v2 = map(int,input().split())

def dijkstra(start):
  cost = [math.inf]*(N+1)
  cost[start] = 0
  heap = []
  heappush(heap, (0,start))

  while heap:
    value, node = heappop(heap)
    for v,nd in graph[node]:
      if cost[nd] > value+v:
        cost[nd] = value+v
        heappush(heap, (value+v, nd))
  
  return cost

d_1 = dijkstra(1)
d_v1 = dijkstra(v1)
d_v2 = dijkstra(v2)
answer = min(d_1[v1]+d_v1[v2]+d_v2[N], d_1[v2]+d_v2[v1]+d_v1[N])

if answer == math.inf:
  print(-1)
else:
  print(answer)