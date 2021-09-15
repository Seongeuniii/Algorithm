import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))
dx,dy = [1, -1, 0, 0], [0, 0, -1, 1]

def bfs(a,b):
    cnt = 0
    queue = deque()
    graph[a][b] = 0
    queue.append((a,b))
    while True:
        try:
            x, y = queue.popleft()
            cnt += 1
            for i in range(4):
                newx = x + dx[i]
                newy = y + dy[i]
                if newy<0  or newy>=n or newx>=n or newx<0:
                    continue
                if graph[newx][newy] == 1:
                    graph[newx][newy] = 0
                    queue.append((newx, newy))
        except:
            return cnt
result = []
num = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            num += 1
            result.append(bfs(x,y))
result.sort()
print(num)
for i in range(len(result)):
    print(result[i])