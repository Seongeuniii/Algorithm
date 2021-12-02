from collections import deque
import sys

N = int(input())
sx,sy,ex,ey = map(int,input().split())

dx,dy = [-2,-2,0,0,2,2], [-1,1,-2,2,-1,1]

visited = [[0]*N for _ in range(N)]
visited[sx][sy] = 1
q = deque()
q.append((sx,sy,0))

while q:
  x,y,c = q.popleft()
  if x==ex and y==ey:
    print(c)
    sys.exit()
  for i in range(6):
    nx,ny = x+dx[i], y+dy[i]
    if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
      visited[nx][ny] = 1
      q.append((nx,ny,c+1))

print(-1)
