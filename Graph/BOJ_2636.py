import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [0,0,1,-1], [1,-1,0,0]

def bfs(sx,sy):
  visited = [[0]*M for _ in range(N)]
  q = deque()
  q.append((sx,sy))
  visited[sx][sy] = 1
  cnt = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
        visited[nx][ny] = 1
        if board[nx][ny]:
          board[nx][ny] = 0
          cnt += 1
        else:
          q.append((nx,ny))
  return cnt

time = 0
answer = 0
while True:
  CNT = bfs(0,0)
  if CNT:
    answer = CNT
  else:
    break
  time += 1

print(time)
print(answer)