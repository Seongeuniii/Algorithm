import sys
from collections import deque 
N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,v = map(int,sys.stdin.readline().split())
    graph[a].append((b,v))
    graph[b].append((a,v))
def bfs(start):
    visited = [0 for _ in range(N+1)]
    queue = deque()
    queue.append((start,0))
    visited[start] = 1
    while queue:
        node,value = queue.popleft()
        if node == END:
            return value
        for l,v in graph[node]:
            if visited[l] == 0:
                queue.append((l,value+v))
                visited[l] = 1
for k in range(M):
    START,END = map(int,sys.stdin.readline().split())
    result = bfs(START)
    print(result)