import sys, math
from heapq import heappush, heappop
n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
result = [math.inf for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
visited = [0 for _ in range(n+1)]
def dijkstra(start):
    heap = []
    result[start] = 0
    heap.append((0,start))
    while heap:
        value, node = heappop(heap)
        if visited[node] == 1:
            continue
        if value > k:
            break
        visited[node] = 1
        for n in graph[node]:
            if value+1 < result[n]:
                result[n] = value+1
                heappush(heap,(result[n],n))
dijkstra(x)
cnt = 0
for i in range(1,n+1):
    if result[i] == k:
        cnt += 1
        print(i)
if cnt == 0:
    print(-1)