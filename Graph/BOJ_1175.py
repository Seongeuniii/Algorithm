import sys,math
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

board = []
for n in range(N):
  line = list(input().strip())
  for m in range(M):
    if line[m] == 'S':
      sx, sy = n, m
  board.append(line)

check = [[[0]*4 for _ in range(M)] for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]

def bfs(sx, sy):
  find_c = False
  q = deque()
  q.append((0, -1, sx, sy ))
  queue = deque()
  qx,qy = 0, 0
  CNT = 0
  
  while q:
    cnt, d, x, y = q.popleft()
    if find_c and CNT-1 > cnt:
      break
    for i in range(4):
      if i == d: continue
      nx,ny = x+dx[i],y+dy[i]

      if 0<=nx<N and 0<=ny<M and board[nx][ny] != '#' and not check[nx][ny][i]:
        check[nx][ny][i] = 1

        if board[nx][ny] == 'C':
          if find_c:
            if nx!=qx or ny!=qy:
              continue
          queue.append((cnt+1, i, nx, ny))
          qx, qy = nx, ny
          find_c = True
          CNT = cnt+1

        q.append((cnt+1, i, nx, ny))
  
  answer = math.inf
  board[qx][qy] = '.'
  for a in range(N):
    for b in range(M):
      for c in range(4):
        check[a][b][c] = 0

  while queue:
    cnt, d, x, y = queue.popleft()
    for i in range(4):
      if i == d: continue
      nx,ny = x+dx[i],y+dy[i]

      if 0<=nx<N and 0<=ny<M and board[nx][ny] != '#' and not check[nx][ny][i]:
        check[nx][ny][i] = 1

        if board[nx][ny] == 'C':
          answer = min(answer, cnt+1)
        else:
          queue.append((cnt+1, i, nx, ny))

  return answer

answer = bfs(sx, sy)
if answer == math.inf:
  print(-1)
else:
  print(answer)