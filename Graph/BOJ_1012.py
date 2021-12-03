import sys
from collections import deque
input = sys.stdin.readline

dx,dy = [0,0,1,-1],[1,-1,0,0]
def bfs(sx,sy):
  q = deque()
  q.append((sx,sy))
  while q:
    x,y = q.popleft()
    for m in range(4):
      nx,ny = x+dx[m], y+dy[m]
      if 0<=nx<N and 0<=ny<M and board[nx][ny]:
        board[nx][ny] = 0
        q.append((nx,ny))

for _ in range(int(input())):
  M,N,K = map(int,input().split())
  board = [[0]*M for _ in range(N)]
  for _ in range(K):
    x,y = map(int,input().split())
    board[y][x] = 1
  
  cnt = 0
  for i in range(N):
    for j in range(M):
      if board[i][j]:
        board[i][j] = 0
        bfs(i,j)
        cnt += 1
  print(cnt)