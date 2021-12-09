import sys
from collections import deque 
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
dx,dy = [0,0,1,-1], [1,-1,0,0]

def bfs(sx,sy):
  q = deque()
  visited = [[0]*M for _ in range(N)]
  q.append((sx,sy,0))
  visited[sx][sy] = 1
  CNT = 0

  while q:
    x,y,c = q.popleft()
    for l in range(4):
      nx,ny = x+dx[l], y+dy[l]
      if 0<=nx<N and 0<=ny<M and board[nx][ny] == 'L' and not visited[nx][ny]:
        visited[nx][ny] = 1
        q.append((nx,ny,c+1))
        CNT = c+1
  
  return CNT

def cannot_set_treasure(tx, ty):
  if 0<tx<N-1:
    if board[tx-1][ty] == board[tx+1][ty] == 'L':
      return 0
  if 0<ty<M-1:
    if board[tx][ty-1] == board[tx][ty+1] == 'L':
      return 0
  return 1
  
answer = 0
for i in range(N):
  for j in range(M):
    if board[i][j] == 'L' and cannot_set_treasure(i, j):
      answer = max(answer, bfs(i,j))
print(answer)