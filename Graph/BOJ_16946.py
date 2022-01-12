import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
wall = [list(map(int,input().strip())) for _ in range(N)]

def bfs(sx,sy):
  dx,dy = [0,0,1,-1], [1,-1,0,0]  

  cnt = 1
  w = []

  q = deque()
  q.append((sx,sy))
  
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      if 0<=nx<N and 0<=ny<M and not check[nx][ny]:
        if wall[nx][ny]:
          check[nx][ny] = 1
          w.append((nx,ny))
        else:
          cnt += 1
          check[nx][ny] = 1
          q.append((nx,ny))

  for x,y in w:
    wall[x][y] += cnt
    check[x][y] = 0

check = [[0]*M for _ in range(N)]
for n in range(N):
  for m in range(M):
    if not wall[n][m] and not check[n][m]:
      check[n][m] = 1
      bfs(n,m)

for i in range(N):
  for j in range(M):
    wall[i][j] = str(wall[i][j] % 10)
  print(''.join(wall[i]))