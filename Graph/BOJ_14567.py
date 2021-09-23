import sys 
from collections import deque
n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indeg[b]+=1

queue = deque()
result = [0 for _ in range(n+1)]

for i in range(1,n+1):
    if indeg[i] == 0:
        queue.append((i,1))
        result[i] = 1

while queue:
    nd,cnt = queue.popleft()
    for l in graph[nd]:
        indeg[l] -= 1
        if indeg[l] == 0:
            queue.append((l,cnt+1))
            result[l] = cnt+1

for j in range(1,n+1):
    print(result[j],end=' ')