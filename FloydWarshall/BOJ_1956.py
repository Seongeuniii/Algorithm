import sys, math
input = sys.stdin.readline

def floydWarshall():
  for k in range(1, V+1):
    for i in range(1, V+1):
      for j in range(1, V+1):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

V, E = map(int, input().split())
dist = [[math.inf]*(V+1) for _ in range(V+1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  dist[a][b] = c

floydWarshall()

answer = []
for i in range(1, V+1):
  for j in range(1, V+1):
    answer.append(dist[i][j] + dist[j][i])

a = min(answer)
if a == math.inf: print(-1)
else: print(a)

import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[math.inf]*(V+1) for _ in range(V+1)]
heap = []

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))
  dist[a][b] = c
  heappush(heap, (c, a, b))

while heap:
  c, a, b = heappop(heap)
  if a == b:
    print(c)
    sys.exit()
  for v, nd in graph[b]:
    if c+v < dist[a][nd]:
      dist[a][nd] = c+v
      heappush(heap, (c+v, a, nd))

print(-1)