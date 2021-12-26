import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
water_q = deque()
gsdc_q = deque()
board = []
for r in range(R):
  b = list(input().strip())
  for c in range(C):
    if b[c] == 'S':
      gsdc_q.append((r,c))
    elif b[c] == '*':
      water_q.append((r,c))
  board.append(b)

dx, dy = [0,0,1,-1], [1,-1,0,0]
check = [[0]*C for _ in range(R)]

def gsdc_bfs(q):
  move = deque()
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<R and 0<=ny<C and not check[nx][ny]:
        check[nx][ny] = 1
        if board[nx][ny] == 'D':
          print(CNT)
          sys.exit()
        elif board[nx][ny] == '.':
          move.append((nx,ny))
  return move

def water_bfs(q):
  move = deque()
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<R and 0<=ny<C:
        if board[nx][ny] == '.':
          board[nx][ny] = '*'
          move.append((nx,ny))
  return move
        
CNT = 0
while gsdc_q:
  CNT += 1
  water_q = water_bfs(water_q)
  gsdc_q = gsdc_bfs(gsdc_q)

print('KAKTUS')