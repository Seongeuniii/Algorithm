import sys
import copy
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def attack(X, board):
  dx, dy = [0,0,-1], [-1,1,0]

  check = [[0]*M for _ in range(N)]
  catch = []
  d = 0
  q = deque([(N, X)])

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
            catch.append([nx, ny])
          else:
            check[nx][ny] = 1
            q.append((nx,ny))

    if catch:
      catch.sort(key=lambda x:x[1])
      return catch[0]
  
  return 0

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

  for case in list(permutations([i for i in range(M)],3)):
    enemy = ENEMY
    kill = 0
    board = copy.deepcopy(BOARD)

    while enemy:
      catch = []
      for x in case:
        catch.append(attack(x, board))
      for c in catch:
        if c and board[c[0]][c[1]]:
          board[c[0]][c[1]] = 0
          kill += 1
          enemy -= 1
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