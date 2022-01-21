import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
  cost[start] = 0
  check[start] = 0

  heap = []
  heappush(heap, (0, 0, start))

  while heap:
    value, c, node = heappop(heap)
    if cost[node] < value:
      continue
    for nd, v in graph[node]:
      if cost[nd] > value + v or (cost[nd] == value + v and not check[nd]):
        if (node == G and nd == H) or (node == H and nd == G) or c == 1:
          check[nd] = 1
          heappush(heap, (value + v, 1, nd))
        elif cost[nd] > value + v :
          check[nd] = 0
          heappush(heap, (value + v, 0, nd))
        cost[nd] = value + v

for _ in range(int(input())):
  N, M, T = map(int,input().split())
  S, G, H = map(int,input().split())
  
  graph = [[] for _ in range(N+1)]
  cost = [math.inf]*(N+1)
  check = [0]*(N+1)

  for _ in range(M):
    a, b, d = map(int,input().split())

    graph[a].append((b,d))
    graph[b].append((a,d))

  dijkstra(S)
  
  answer = []
  for _ in range(T):
    cdd = int(input())
    if check[cdd]:
      answer.append(cdd)

  print(' '.join(map(str,sorted(answer))))