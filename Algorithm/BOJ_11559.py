import sys
from collections import deque
input = sys.stdin.readline

field = [deque() for _ in range(6)]

for _ in range(12):
  for i, x in enumerate(list(input().strip())):
    if x != '.':
      field[i].appendleft(x)

dx, dy = [0,0,1,-1], [1,-1,0,0]
def bfs(x, y):
  xy = [(x, y)]
  q = deque([(x, y)])
  cnt = 0

  while q:
    cnt += 1
    x, y = q.popleft()

    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<6 and 0<=ny<len(field[nx]) and not check[nx][ny] and field[x][y] == field[nx][ny]:
        check[nx][ny] = 1
        xy.append((nx, ny))
        q.append((nx, ny))

  if cnt >= 4:
    for x, y in xy:
      check[x][y] = 2
    return 1
  
  return 0

answer = 0
flag = True

while flag:
  flag = False
  check = [[0]*12 for _ in range(6)]
  
  for i in range(6):
    for j in range(len(field[i])):
      if not check[i][j]:
        check[i][j] = 1
        if bfs(i, j): flag = True
  
  if flag:
    answer += 1
    newfield = [[] for _ in range(6)]

    for i in range(6):
      for j in range(len(field[i])):
        if check[i][j] != 2:
          newfield[i].append(field[i][j])

    field = newfield

print(answer)