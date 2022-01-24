import sys
from collections import deque
input = sys.stdin.readline

def bfs(sx,sy):
  check = [[0]*M for _ in range(N)]
  q = deque()

  check[sx][sy] = 1
  q.append((sx,sy))
  cnt = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<M:
        if board[nx][ny]:
          if check[nx][ny]:
            board[nx][ny] = 0
            cnt += 1
          else:
            check[nx][ny] += 1
        elif not check[nx][ny]:
          check[nx][ny] = 1
          q.append((nx,ny))

  return cnt

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [0,0,1,-1], [1,-1,0,0]

answer = 0

while True:
  cnt = bfs(0,0)
  if cnt:
    answer += 1
  else: 
    break

print(answer)