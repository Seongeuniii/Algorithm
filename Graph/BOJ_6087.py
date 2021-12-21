import sys, math
from heapq import heappush,heappop
input = sys.stdin.readline

W,H = map(int,input().split())
mirror = [[math.inf for _ in range(W)] for _ in range(H)]
cx, cy = [0,0], [0,0] # C 위치
c = 0

board = []
for h in range(H):
  line = list(input().strip())
  for w in range(W):
    if line[w] == 'C':
      cx[c],cy[c] = h,w
      c += 1
  board.append(line)

dx, dy = [0,0,1,-1], [1,-1,0,0]

def dijkstra(x, y):
    heap = []
    mirror[x][y] = 0
    heappush(heap, (0,-1,x,y))

    while heap:
      cnt, d, x, y = heappop(heap)

      for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<H and 0<=ny<W and board[nx][ny] != '*':

          if i == d or d==-1:
            nc = cnt
          else:
            nc = cnt+1

          if nc <= mirror[nx][ny]:
              mirror[nx][ny] = nc
              heappush(heap, (mirror[nx][ny],i,nx,ny))

dijkstra(cx[0],cy[0])

print(mirror[cx[1]][cy[1]])