import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = []
dx,dy = [0,0,1,-1], [1,-1,0,0]

for i in range(N):
  line = list(map(int,input().split()))
  for j in range(M):
    if line[j] == 2:
      line[j] = 0
      sx,sy = i,j
  board.append(line)

visited = [[0]*M for _ in range(N)]

def bfs(xx,yy):
  q = deque()
  q.append((xx,yy,0))
  visited[xx][yy] = 1
  while q:
    x,y,c = q.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and board[nx][ny]:
        visited[nx][ny] = 1
        board[nx][ny] = c+1
        q.append((nx,ny,c+1))

bfs(sx,sy)

for a in range(N):
  for b in range(M):
    if not visited[a][b] and board[a][b]:
      board[a][b] = -1
  print(' '.join(map(str,board[a])))