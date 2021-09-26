import sys, math
from heapq import heappush, heappop
num,e = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(num+1)]
result = [math.inf for _ in range(num+1)]
for _ in range(e):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((w,v))

visited = [0 for _ in range(num+1)]
def dijkstra(start):
    heap = []
    result[start] = 0
    visited[start] = 0
    heappush(heap,(0,start))
    while heap:
        value,node = heappop(heap)
        visited[node] = 1
        for v,n in graph[node]:
            if visited[n] == 0:
                if value + v < result[n]:
                    result[n] = value + v
                    heappush(heap,(result[n],n))
dijkstra(k)
for i in range(1,num+1):
    if result[i] == math.inf:
        print('INF')
    else:
        print(result[i])