import sys
from collections import deque
input = sys.stdin.readline

q = deque()
tomato = 0
box = []

M,N = map(int,input().split())

for i in range(N):
  line = list(map(int,input().split()))
  box.append(line)
  for j in range(M):
    if line[j] == 0:
      continue
    if line[j] == 1:
      q.append((i,j,0))
    tomato += 1

dx,dy = [0,0,1,-1], [1,-1,0,0]
answer = 0

while q:
  x, y, c = q.popleft()
  answer = max(answer, c)
  for t in range(4):
    nx, ny = x+dx[t], y+dy[t]
    if  0<=nx<N and 0<=ny<M:
      if box[nx][ny] == 0:
        box[nx][ny] = 1
        tomato += 1
        q.append((nx,ny,c+1))

if tomato < M*N:
  print(-1)
else:
  print(answer)

