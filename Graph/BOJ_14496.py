import sys
from collections import deque
a,b = map(int,sys.stdin.readline().split())
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
queue = deque([])
queue.append((0,a))
visited = [0 for _ in range(n+1)]
visited[a] = 1
cnt = 0
while queue:
    cnt, start = queue.popleft()
    if start == b: 
        print(cnt)
        sys.exit()
    for l in graph[start]:
        if visited[l] == 0:
            visited[l] = 1
            queue.append((cnt+1,l))
print(-1)