import sys
input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
wall = [list(map(int,input().split())) for _ in range(N)]

left = {0:[0,-1,3], 1:[-1,0,0], 2:[0,1,1], 3:[1,0,2]}
back = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}

def bfs(sx,sy,sd):
  clean = [[0 for _ in range(M)] for _ in range(N)]
  clean[sx][sy] = 1
   
  x,y,d = sx,sy,sd
  answer = 1
  
  while True:
    nx, ny = x+left[d][0], y+left[d][1]
    if 0<=nx<N and 0<=ny<M and not wall[nx][ny] and not clean[nx][ny]:
      x, y, d = nx, ny, left[d][2]
      clean[x][y] = 1
      answer += 1
    else:
      if clean[x][y] < 4:
        clean[x][y] += 1
        d = left[d][2]
      else:
        bx,by = x+back[left[d][2]][0], y+back[left[d][2]][1]
        if bx<0 or bx>=N or by<0 or by>=M or wall[bx][by]:
          return answer
        else:
          x, y, d = bx, by, left[d][2]
          if not clean[x][y]:
            answer += 1
          clean[x][y] = 1
    
print(bfs(r,c,d))