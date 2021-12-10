import sys
from collections import deque 
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [0,0,1,-1], [1,-1,0,0]

def bfs(sx,sy):
  q = deque()
  visited = [[0]*M for _ in range(N)]
  q.append((sx,sy,0))
  visited[sx][sy] = 1
  num = 0
  CNT = 0

  while q:
    x,y,c = q.popleft()
    for l in range(4):
      nx,ny = x+dx[l], y+dy[l]
      if 0<=nx<N and 0<=ny<M and board[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        q.append((nx,ny,c+1))
        if c+1 > CNT:
          CNT = c+1
          num = board[nx][ny]
        else:
          num = max(board[nx][ny],num)
  return [CNT,num]

def test(tx, ty):
  if 0<tx<N-1:
    if board[tx-1][ty] and board[tx+1][ty]:
      return 0
  if 0<ty<M-1:
    if board[tx][ty-1] and board[tx][ty+1]:
      return 0
  return 1
  
cnt = 0
answer = 0
for i in range(N):
  for j in range(M):
    if board[i][j] and test(i, j):
      li = bfs(i,j)
      if li[0] > cnt:
        cnt = li[0]
        answer = board[i][j]+li[1]
      elif li[0] == cnt:
        answer = max(answer, board[i][j]+li[1])

print(answer)