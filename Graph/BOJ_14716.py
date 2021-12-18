import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]
dx,dy = [0,0,1,-1,1,-1,1,-1], [1,-1,0,0,1,-1,-1,1] 

def bfs(sx,sy):
  q = deque()
  q.append((sx,sy))
  while q:
    x,y = q.popleft()
    for i in range(8):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<M and 0<=ny<N and board[nx][ny]:
        board[nx][ny] = 0
        q.append((nx,ny))

answer = 0
for a in range(M):
  for b in range(N):
    if board[a][b]:
      board[a][b] = 0
      bfs(a,b)
      answer += 1

print(answer)