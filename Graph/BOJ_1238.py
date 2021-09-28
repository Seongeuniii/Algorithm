import sys,math
from heapq import heappop,heappush, merge
N,M,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
graph_reverse = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append((t,b))
    graph_reverse[b].append((t,a))
heap = []
def dijkstra(start,G):
    result = [math.inf for _ in range(N+1)]
    heappush(heap,(0,start))
    result[start] = 0
    while heap:
        value, node = heappop(heap)
        for v,nd in G[node]:
            if result[nd] > value + v:
                result[nd] = value + v
                heappush(heap,(result[nd],nd))
    return result
dep = dijkstra(X,graph_reverse)
end = dijkstra(X,graph)
a = 0
for i in range(1,N+1):
    a = max(a,dep[i]+end[i])
print(a)