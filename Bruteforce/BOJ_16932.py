import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dic = {}
check = [[0]*M for _ in range(N)]
dx,dy = [1,-1,0,0], [0,0,1,-1]

def bfs(sx,sy,idx):
  cnt = 1
  q = deque()
  q.append((sx,sy))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<N and 0<=ny<M and board[nx][ny] and not check[nx][ny]:
        cnt += 1
        check[nx][ny] = idx
        q.append((nx,ny))
  return cnt

idx = 1
for n in range(N):
  for m in range(M):
    if not check[n][m] and board[n][m]:
      check[n][m] = idx
      dic[idx] = bfs(n,m,idx)
      idx += 1

answer = 0
for n in range(N):
  for m in range(M):
    if not board[n][m]:
      test = {}
      for i in range(4):
        nx, ny = n+dx[i], m+dy[i]
        if 0<=nx<N and 0<=ny<M and check[nx][ny]:
          c = check[nx][ny]
          try: test[c] = max(test[c], dic[c])
          except: test[c] = dic[c]
      answer = max(sum(test.values())+1,answer)
print(answer)