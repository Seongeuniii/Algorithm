import sys,math
from heapq import heappop,heappush
N,M,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)] 
for _ in range(M):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append((t,b))
heap = []
party = []
def dijkstra(start):
    global party
    result = [math.inf for _ in range(N+1)]
    heappush(heap,(0,start))
    result[start] = 0
    while heap:
        value, node = heappop(heap)
        for v,nd in graph[node]:
            if result[nd] > value + v:
                result[nd] = value + v
                heappush(heap,(result[nd],nd))
    if start == X:
        party = result
    return result[X]
li = [0]
for i in range(1,N+1):
    a = dijkstra(i)
    li.append(a)
for j in range(1,N+1):
    li[j] = li[j]+party[j]
print(max(li))