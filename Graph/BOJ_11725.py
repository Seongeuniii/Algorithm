import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

queue = deque()
queue.append(1)
visited[1] = 1
while queue:
    nd = queue.popleft()
    for l in graph[nd]:
        if visited[l] == 0:
            result[l] = nd
            visited[l] = 1
            queue.append(l)
for i in range(2,n+1):
    print(result[i])