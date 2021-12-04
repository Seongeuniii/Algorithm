import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

board = [list(map(int,input().strip())) for _ in range(N)]
dx,dy = [0,0,1,-1], [1,-1,0,0]

check = [[0]*M for _ in range(N)]
check1 = [[0]*M for _ in range(N)]

q = deque()
if 0 == N-1 and 0 == M-1:
  print(1)
  sys.exit()
else:
  q.append((0,0,1,0)) #cnt, break

while q:
  x,y,c,b = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0<=nx<N and 0<=ny<M:
      if nx == N-1 and ny == M-1:
        print(c+1)
        sys.exit()
      if b: # 이미 벽을 부심
        if not board[nx][ny] and not check1[nx][ny]: # 벽이 없고
          check1[nx][ny] = 1
          q.append((nx,ny,c+1,b))
      else: # 벽 안부심
        if board[nx][ny] and not check1[nx][ny]: # 벽이 있고
          check1[nx][ny] = 1
          q.append((nx,ny,c+1,1))
        elif not board[nx][ny] and not check[nx][ny]: # 벽이 없고
          check[nx][ny] = 1
          q.append((nx,ny,c+1,b))
print(-1)