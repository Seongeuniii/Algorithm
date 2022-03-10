import sys
import copy
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def attack(case, board):
  dx, dy = [0,0,-1], [-1,1,0]
  catch = set()

  for x in case:
    d = 0
    check = [[0]*M for _ in range(N)]
    q = deque([(N, x)])
    c = []

    while q and d < D:
      d += 1
      nq = q
      q = deque()

      while nq:
        x, y = nq.popleft()
        for i in range(3):
          nx, ny = x+dx[i], y+dy[i]
          if 0 <= nx < N and 0 <= ny <M and not check[nx][ny]:
            if board[nx][ny]:
              c.append((nx, ny))
            else:
              check[nx][ny] = 1
              q.append((nx,ny))

      if c:
        catch.add(sorted(c, key=lambda x:x[1])[0])
        break

  if catch:
    for x, y in catch:
      board[x][y] = 0
  
  return len(catch)

def move(board):
  cnt = 0

  for n in range(N-1, -1, -1):
    for m in range(M):
      if board[n][m]:
        board[n][m] = 0
        if n+1 == N:
          cnt += 1
        else:
          board[n+1][m] = 1
  
  return cnt

def solution():
  answer = 0

  for case in list(permutations(range(M),3)):
    enemy = ENEMY
    kill = 0
    board = copy.deepcopy(BOARD)

    while enemy:
      result = attack(case, board)
      kill += result
      enemy -= result

      if enemy:
        enemy -= move(board)

    answer = max(answer, kill)

  return answer

N, M, D = map(int,input().split())
BOARD = []
ENEMY = 0

for i in range(N):
  BOARD.append(list(map(int,input().split())))
  ENEMY += BOARD[i].count(1)

print(solution())

