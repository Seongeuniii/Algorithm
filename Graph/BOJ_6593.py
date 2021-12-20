import sys
from collections import deque
input = sys.stdin.readline

dx, dy, dz = [0,0,1,-1,0,0], [0,0,0,0,1,-1], [1,-1,0,0,0,0] 

def bfs(sx, sy, sz, L, R, C):
  q = deque()
  q.append((sx,sy,sz,0))
  building[sz][sx][sy] = '#'

  while q:
    x, y, z, cnt = q.popleft()
    for i in range(6):
      nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]

      if 0<=nx<R and 0<=ny<C and 0<=nz<L:
        if building[nz][nx][ny] == 'E':
          return cnt+1
        elif building[nz][nx][ny] == '.':
          building[nz][nx][ny] = '#'
          q.append((nx,ny,nz,cnt+1))

while True:
  try:
    L,R,C = map(int,input().split())
    building = []
    for l in range(L):
      floor = []
      for r in range(R):
        f = list(input().strip())
        for c in range(C):
          if f[c] == 'S':
            sx, sy, sz = r, c, l
        floor.append(f)
      building.append(floor)
      upstair = input()  

    answer = bfs(sx, sy, sz, L, R, C)
    if answer:
      print("Escaped in", answer,"minute(s).")
    else:
      print("Trapped!")
      
  except:
    exit()