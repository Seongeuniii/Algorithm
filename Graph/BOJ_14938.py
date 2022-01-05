import sys,math
from heapq import heappop,heappush
input = sys.stdin.readline

N,M,R = map(int,input().split())
item = [0] + list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
  a,b,c = map(int,input().split())
  graph[a].append((c,b))
  graph[b].append((c,a))

def dijkstra(start):
  result = 0
  cost = [math.inf]*(N+1)
  pickup = [0]*(N+1)

  cost[start] = 0
  pickup[start] = 1
  result += item[start]

  heap = []
  heappush(heap,(0,start))

  while heap:
    value, node = heappop(heap)
    for v,nd in graph[node]:
      if value + v > M:
        continue
      if cost[nd] > value+v:
        cost[nd] = value+v
        heappush(heap,(value+v, nd))
        if not pickup[nd]:
          pickup[nd] = 1
          result += item[nd]

  return result

answer = 0
for i in range(1,N):
  answer = max(answer, dijkstra(i))
print(answer)