import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(sx, sy):
  cnt = 0
  q = deque()
  q.append((sx,sy))
  check[sx][sy] = 1

  while q:
    cnt += 1
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<M and not check[nx][ny] and board[nx][ny] == 0:
        check[nx][ny] = 1
        q.append((nx,ny))

  return cnt

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
not_wall = []
wall = 3
virus = []

for n in range(N):
  for m in range(M):
    if board[n][m] == 0:
      not_wall.append((n,m))
    elif board[n][m] == 2:
      virus.append((n,m))
    else:
      wall += 1

answer = 0
for w1, w2, w3 in list(combinations(not_wall,3)):
  board[w1[0]][w1[1]] = 1
  board[w2[0]][w2[1]] = 1
  board[w3[0]][w3[1]] = 1

  check = [[0]*M for _ in range(N)]
  cnt = 0
  for vx, vy in virus:
    if not check[vx][vy]:
      cnt += bfs(vx,vy)
  answer = max(answer, N*M-wall-cnt)

  board[w1[0]][w1[1]] = 0
  board[w2[0]][w2[1]] = 0
  board[w3[0]][w3[1]] = 0

print(answer)