import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for _ in range(N)]
for p in range(N):
  graph[p] = list(map(int,input().split()))
dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs(sx,sy):
  global graph, visited
  newgraph = graph
  visited[sx][sy] = 1
  queue = deque()
  queue.append((sx,sy))
  while queue:
    cnt = 0
    x, y = queue.popleft()
    for k in range(4):
      newx, newy = x+dx[k], y+dy[k]
      if 0<=newx<N and 0<=newy<M:
        if visited[newx][newy] == 0:
          if graph[newx][newy] <= 0:
            cnt += 1
          else:
            visited[newx][newy] = 1
            queue.append((newx,newy))
    newgraph[x][y] -= cnt
  return newgraph
time = 0
move = True
while move:
  move = False
  visited = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(1,N-1):
    for j in range(1,M-1):
      if graph[i][j] > 0 and visited[i][j] == 0:
        if move == True:
          print(time)
          sys.exit()
        else:
          move = True
          nextgraph = bfs(i,j)
  graph = nextgraph
  time += 1
print(0)