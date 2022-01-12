import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
wall = [list(map(int,input().strip())) for _ in range(N)]

def bfs(sx,sy,k):
  if sx == N-1 and sy == M-1:
    return 1

  dx,dy = [0,0,1,-1], [1,-1,0,0]  
  check = [[K+1]*M for _ in range(N)]

  answer = 0
  q = deque()
  temp = deque()
  temp.append((0,0,0))

  while temp:
    q = temp
    answer += 1

    temp = deque()
    while q:
      x,y,b = q.popleft()
      for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<N and 0<=ny<M:
          if nx == N-1 and ny == M-1:
            return answer+1

          if wall[nx][ny]:
            if b < k and check[nx][ny] > b+1:
                check[nx][ny] = b+1
                temp.append((nx,ny,b+1))

          elif check[nx][ny] > b:
              check[nx][ny] = b
              temp.append((nx,ny,b))

  return -1

print(bfs(0,0,K))