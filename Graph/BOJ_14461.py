import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(sx, sy):
  dx, dy = [0,0,1,-1], [1,-1,0,0]
  dist = [[[math.inf]*3 for _ in range(N)] for _ in range(N)]
  heap = []

  dist[sx][sy] = [0, 0, 0]
  heappush(heap, (0, 0, sx, sy))

  while heap:
    d, c, x, y = heappop(heap)
    
    if dist[x][y][c] < d: continue
    
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<N:
        if c+1 == 3:
          if dist[nx][ny][0] > d + T + time[nx][ny]:
            dist[nx][ny][0] = d + T + time[nx][ny]
            heappush(heap, (dist[nx][ny][0], 0, nx, ny))
        elif dist[nx][ny][c+1] > d + T:
            dist[nx][ny][c+1] = d + T
            heappush(heap, (dist[nx][ny][c+1], c+1, nx, ny))

  print(min(dist[N-1][N-1]))
  
N, T = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(N)]
dijkstra(0, 0)
