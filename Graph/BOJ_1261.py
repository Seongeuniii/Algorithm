import sys,math
from heapq import heappop,heappush
M,N = map(int,sys.stdin.readline().split())
result = [[math.inf for _ in range(M+1)] for _ in range(N+1)]
graph = [[0] for _ in range(N+1)]
for i in range(1,N+1):
    graph[i].extend(map(int,sys.stdin.readline().strip()))
dx,dy = [0,0,1,-1], [1,-1,0,0]
heap = []
def dijkstra(sx,sy):
    result[sx][sy] = 0
    heappush(heap,(0,sx,sy))
    while heap:
        value, x, y = heappop(heap)
        for i in range(4):
            newx, newy = x + dx[i], y + dy[i]
            if 0<newx<=N and 0<newy<=M:
                if result[newx][newy] > graph[newx][newy]+value:
                    result[newx][newy] = graph[newx][newy]+value
                    heappush(heap,(result[newx][newy],newx,newy))
dijkstra(1,1)
print(result[N][M])