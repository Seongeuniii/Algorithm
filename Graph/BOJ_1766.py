import sys
from heapq import heappop,heappush
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indeg[b] += 1
heap  = []
for i in range(1,n+1):
    if indeg[i] == 0:
        heappush(heap,i)
result = []
while heap:
    nd = heappop(heap)
    result.append(nd)
    for l in graph[nd]:
        indeg[l] -= 1
        if indeg[l] == 0:
            heappush(heap,l)
for k in range(n):
    print(result[k],end=' ')