import sys, math
from heapq import heappush,heappop
n = int(sys.stdin.readline())
cnt = 1
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
            if newx < 0 or newx >=n or newy<0 or newy >= n:
                continue
            if visited[newx][newy] == 0:
                if value + graph[newx][newy] < result[newx][newy]:
                    result[newx][newy] = value + graph[newx][newy]
                    heappush(heap, (result[newx][newy],newx,newy))

while n != 0:
    graph = []
    result = [[math.inf for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    visited = [[0 for _ in range(n)] for _ in range(n)]

    dijkstra(graph[0][0],0,0)
    print('Problem', cnt, end='')
    print(':', result[n-1][n-1])
    cnt += 1 
    n = int(sys.stdin.readline())