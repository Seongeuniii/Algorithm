import sys,math
from heapq import heappop, heappush
input = sys.stdin.readline

N,M,T,D = map(int,input().split())
board = [[i-65 if i < 97 else i-71 for i in list(map(ord,input().strip()))] for _ in range(N)]

def dijkstra(sx, sy):
  dx, dy = [0,0,1,-1], [1,-1,0,0]

  up_time = [[math.inf]*M for _ in range(N)]
  down_time = [[math.inf]*M for _ in range(N)]
  heap = []

  up_time[sx][sy] = 0
  down_time[sx][sy] = 0
  heappush(heap, (0,1,sx,sy)) # up은 1 down은 0
  heappush(heap, (0,0,sx,sy))

  while heap:
    c,ud,x,y = heappop(heap)
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<M:
        diff = abs(board[x][y]-board[nx][ny])
        if ud:
          if diff <= T:
            if board[nx][ny] > board[x][y]: # 더 높은 곳
              if up_time[nx][ny] > c + diff**2:
                up_time[nx][ny] = c + diff**2
                heappush(heap, (c+diff**2, ud, nx, ny))
            elif up_time[nx][ny] > c + 1:
              up_time[nx][ny] = c + 1
              heappush(heap, (c+1, ud, nx, ny))
        else:
          if diff <= T:
            if board[nx][ny] < board[x][y]:
              if down_time[nx][ny] > c + diff**2:
                down_time[nx][ny] = c + diff**2
                heappush(heap, (c+diff**2, ud, nx, ny))
            elif down_time[nx][ny] > c + 1:
              down_time[nx][ny] = c + 1
              heappush(heap, (c+1, ud, nx, ny))
  answer = 0
  for n in range(N):
    for m in range(M):
      if up_time[n][m] + down_time[n][m] <= D:
        answer = max(answer, board[n][m])
  return answer

print(dijkstra(0,0))