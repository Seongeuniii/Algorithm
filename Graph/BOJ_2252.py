import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indeg[b] += 1
queue = deque()
for i in range(1,n+1):
    if indeg[i] == 0:
        queue.append(i)
result = []
while queue:
    nd = queue.popleft()
    result.append(nd)
    for l in graph[nd]:
        indeg[l] -= 1
        if indeg[l] == 0:
            queue.append(l)
for k in range(n):
    print(result[k],end=' ')