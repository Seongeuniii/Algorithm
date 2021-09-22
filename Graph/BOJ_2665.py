import sys, math
from heapq import heappush,heappop
n = int(sys.stdin.readline())
graph = [[0] for _ in range(n+1)]
result = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i].extend(map(int,sys.stdin.readline().strip()))

visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
dx, dy = [0,0,1,-1], [1,-1,0,0]

def dijkstra(v, a, b):
    heap = []
    result[a][b] = v
    heappush(heap, (v,a,b))
    while heap:
        value, x, y = heappop(heap)
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1
        for i in range(4):
            newx,newy = x+dx[i],y+dy[i]
            if newx<1 or newx>n or newy<1 or newy>n:
                continue
            if visited[newx][newy] == 0:
                if graph[newx][newy] == 1:
                    a = 0
                else:
                    a = 1
                if value + a < result[newx][newy]:
                    result[newx][newy] = value + a
                    heappush(heap, (result[newx][newy],newx,newy))
dijkstra(0,1,1)
print(result[n][n])