import sys,math
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dx, dy = [0,0,1,-1], [1,-1,0,0] 
check = [[0]*N for _ in range(N)]
b_q = deque()

def ground(sx,sy,num):
  q = deque()
  q.append((sx,sy))
  while q:
    x,y = q.popleft()
    board[x][y] = num
    for d in range(4):
      nx, ny = x+dx[d], y+dy[d]
      if 0<=nx<N and 0<=ny<N:
        if board[nx][ny] and not check[nx][ny]:
          check[nx][ny] = 1
          q.append((nx,ny))
        elif not board[nx][ny]:
          b_q.append((x,y,num))

def bridge(sx,sy,num):
  global answer
  b_check = [[0]*N for _ in range(N)]
  q = deque()
  q.append((sx,sy,0))
  while q:
    x,y,cnt = q.popleft()
    for d in range(4):
      nx, ny = x+dx[d], y+dy[d]
      if 0<=nx<N and 0<=ny<N:
        if board[nx][ny] and board[nx][ny] != num:
          answer = min(answer,cnt)
        elif not board[nx][ny] and not b_check[nx][ny] and cnt < answer-1:
          b_check[nx][ny] = 1
          q.append((nx,ny,cnt+1))

num = 1
for i in range(N):
  for j in range(N):
    if board[i][j] and not check[i][j]:
      check[i][j] = 1
      ground(i,j,num)
      num += 1

answer = math.inf
while b_q:
  x,y,num = b_q.popleft()
  bridge(x,y,num)

print(answer)