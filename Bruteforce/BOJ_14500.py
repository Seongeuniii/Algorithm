import sys
input = sys.stdin.readline
poly = [
    [(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], 
    [(0,1), (1,0), (1,1)],
    [(1,0), (2,0), (2,1)], [(1,0), (2,0), (2,-1)], 
    [(0,1), (0,2), (-1,2)],[(0,1), (0,2), (1,2)],
    [(0,1), (1,1), (2,1)], [(0,1), (1,0), (2,0)],
    [(0,1), (0,2), (1,0)], [(-1,0), (0,1), (0,2)],
    [(0,-1), (0,1), (1,0)], [(0,-1), (0,1), (-1,0)], [(1,0), (-1,0), (0,-1)], [(1,0), (-1,0), (0,1)],
    [(1,0), (1,1), (2,1)], [(1,0), (1,-1), (2,-1)], [(0,1), (-1,1), (-1,2)], [(0,1), (1,1), (1,2)]
]
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
result = 0
for i in range(N):
  for j in range(M):
    for l in poly:
      test = board[i][j]
      for dx,dy in l:
        if 0<=i+dx<N and 0<=j+dy<M:
          test += board[i+dx][j+dy]
        else:
          break
      result = max(result, test)
print(result)