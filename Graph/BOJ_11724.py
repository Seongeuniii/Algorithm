import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
queue = deque()

def bfs(n):
    queue.append(n)
    while queue:
        start = queue.popleft()
        for l in graph[start]:
            if visited[l] == 0:
                queue.append(l)
                visited[l] = 1

cnt = 0
for i in range(1,n+1):
    if visited[i] == 0:
        visited[i] = 1
        bfs(i)    
        cnt += 1
print(cnt)