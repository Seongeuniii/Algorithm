from collections import deque
N = int(input())
board = [input() for _ in range(N)]
dx,dy = [0,0,-1,1], [1,-1,0,0]
def bfs1(c,sx,sy):
  code = c
  q = deque()
  q.append((sx,sy))
  while q:
    x,y = q.popleft()
    for m in range(4):
      nx,ny = x+dx[m], y+dy[m]
      if 0<=nx<N and 0<=ny<N:
        if not visited[nx][ny] and board[nx][ny] == code:
          visited[nx][ny] = 1
          q.append((nx,ny))
def bfs2(sx,sy):
  q = deque()
  q.append((sx,sy))
  while q:
    x,y = q.popleft()
    for m in range(4):
      nx,ny = x+dx[m], y+dy[m]
      if 0<=nx<N and 0<=ny<N:
        if not visited[nx][ny] and board[nx][ny] != 'B':
          visited[nx][ny] = 1
          q.append((nx,ny))
visited = [[0 for _ in range(N)] for _ in range(N)]
result1 = 0
B = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      visited[i][j] = 1
      bfs1(board[i][j],i,j)
      result1 += 1
      if board[i][j] == 'B':
        B+=1
visited = [[0 for _ in range(N)] for _ in range(N)]
result2 = B
for a in range(N):
  for b in range(N):
    if not visited[a][b] and board[a][b] != 'B':
      visited[a][b] = 1
      bfs2(a,b)
      result2 += 1
print(result1,result2)