import sys
from collections import deque

N,M = map(int,input().split())
board = [0]*101
visited = [0]*101

for _ in range(N+M):
  x,y = map(int,input().split())
  board[x] = y

q = deque()
q.append((1,0))

while q:
  nd, c = q.popleft()
  for i in range(1,7):
    move = nd+i

    if 0 < move < 101 and not visited[move]:
      visited[move] = 1

      if move == 100:
        print(c+1)
        sys.exit()
      elif board[move]:
        visited[board[move]] = 1
        q.append((board[move],c+1))
      else:
        q.append((move,c+1))
