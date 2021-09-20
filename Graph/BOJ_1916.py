import sys
from heapq import heappush, heappop
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = 1000000000000000
result = [inf for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,value = map(int,sys.stdin.readline().split())
    graph[a].append((value,b))
start,end = map(int,sys.stdin.readline().split())
visited = [0 for _ in range(n+1)]
def dijkstra(start):
    heap = []
    result[start] = 0
    heappush(heap, (0,start))
    while heap:
        value, node = heappop(heap)
        if visited[node] == 1:
            continue
        visited[node] = 1
        for v,n in graph[node]:
            if value+v < result[n]:
                result[n] = value+v
                heappush(heap,(result[n],n))
dijkstra(start)
print(result[end])