import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def bfs(height, a, b):
    queue.append((height,a,b))
    while queue:
        height, x, y = queue.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newy<0  or newy>=n or newx>=n or newx<0:
                continue
            if graph[newx][newy] > height and visited[newx][newy] == 0:
                visited[newx][newy] = 1
                queue.append((height, newx, newy))
max_num = 1
for height in range(100):
    result = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > height:
                visited[i][j] = 1
                bfs(height,i,j)
                result += 1
    max_num = max(max_num,result)
print(max_num)          