import sys, math
from heapq import heappop, heappush

input = sys.stdin.readline

def djikstra(start):
  dist = [math.inf]*(N+1)
  heap = []

  dist[start] = 0
  heappush(heap, (0, start))

  while heap:
    dst, node = heappop(heap)
    if dist[node] < dst: continue

    for nd, d in graph[node]:
      if dst + d < dist[nd]:
        dist[nd] = dst + d
        heappush(heap, (dst + d, nd))
  
  a_li, b_li = [], []

  for a in A:
    a_li.append(dist[a])
  for b in B:
    b_li.append(dist[b])

  a_answer = min(a_li)
  b_answer = min(b_li)

  if a_answer == math.inf and b_answer == math.inf:
    print(-1)
  elif a_answer <= b_answer:
    print('A')
    print(a_answer)
  else:
    print('B')
    print(b_answer)

N, M = map(int, input().split())
J = int(input())
K = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(M):
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, Z))
  graph[Y].append((X, Z))

djikstra(J)