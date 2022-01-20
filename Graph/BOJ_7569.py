import sys
from collections import deque
input = sys.stdin.readline

def bfs(q):
  global tomato
  ripe = deque()

  while q:
    z,x,y = q.popleft()
    for i in range(6):
      nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
      if 0<=nx<N and 0<=ny<M and 0<=nz<H:
        if not box[nz][nx][ny]:
          tomato -= 1
          box[nz][nx][ny] = -1
          ripe.append((nz,nx,ny))

  return ripe

M,N,H = map(int,input().split())
dx,dy,dz = [0,0,1,-1,0,0], [1,-1,0,0,0,0], [0,0,0,0,1,-1]
box = []
tomato = 0
answer = 0
q = deque()

for h in range(H):
  floor = []
  for n in range(N):
    line = list(map(int,input().split()))
    for m in range(M):
      if line[m] == 1:
        line[m] = -1
        q.append((h,n,m))
      elif not line[m]:
        tomato += 1
    floor.append(line)
  box.append(floor)

while q and tomato:
  answer += 1
  q = bfs(q)

if not tomato:
  print(answer)
else:
  print(-1)