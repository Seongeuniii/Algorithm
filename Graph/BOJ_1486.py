import sys,math
from heapq import heappop, heappush
input = sys.stdin.readline

N,M,T,D = map(int,input().split())
board = [list(map(ord,input().strip())) for _ in range(N)]

for n in range(N):
  for m in range(M):
    if board[n][m] > 96: board[n][m] -= 71
    else: board[n][m] -= 65

def dijkstra(sx, sy):
  dx, dy = [0,0,1,-1], [1,-1,0,0]

  time = [[math.inf]*M for _ in range(N)]
  heap = []

  time[sx][sy] = 0
  heappush(heap, (0,sx,sy))

  while heap:
    c,x,y = heappop(heap)
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<M:
        diff = abs(board[x][y]-board[nx][ny])

        if diff <= T:
          if board[nx][ny] > board[x][y]: # 더 높은 곳
            if time[nx][ny] > c + diff**2:
              time[nx][ny] = c + diff**2
              heappush(heap, (c+diff**2, nx, ny))
          elif time[nx][ny] > c + 1:
            time[nx][ny] = c + 1
            heappush(heap, (c+1, nx, ny))
  
  return time

time = dijkstra(0,0)
answer = 0
for i in range(N):
  for j in range(M):
    t = dijkstra(i,j)
    if time[i][j] + t[0][0] <= D:
      answer = max(answer, board[i][j])
print(answer)