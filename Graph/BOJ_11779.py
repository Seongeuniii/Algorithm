import sys,math
from heapq import heappop,heappush
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
result = [math.inf]*(N+1)
parent = [0]*(N+1)
answer = []

for _ in range(M):
  a,b,v = map(int,input().split())
  graph[a].append((v,b))

S,E = map(int,input().split())

def dijkstra(start):
  heap = []
  result[start] = 0
  heappush(heap,(0,start))
  while heap:
    value, node = heappop(heap)
    if value > result[node]:
      continue
    for v,nd in graph[node]:
      if value + v < result[nd]:
        result[nd] = value + v
        parent[nd] = node
        heappush(heap, (result[nd],nd))

def dfs(start):
  node = start
  while True:
    answer.append(node)
    node = parent[node]
    if node == S:
      answer.append(node)
      return

dijkstra(S)
dfs(E)

print(result[E])
print(len(answer))
for l in answer[::-1]:
  print(l, end=' ')