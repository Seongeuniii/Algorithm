import sys
input = sys.stdin.readline

def chess(n, m, flag):
  cnt = 0

  for i in range(8):
    for j in range(8):
      if board[n+i][m+j] != line[flag][j]:
        cnt += 1

    flag = ~flag
  
  return cnt

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
line = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
answer = 2500

for n in range(N-7):
  for m in range(M-7):
    answer = min(answer, chess(n, m, 0), chess(n, m, 1))

print(answer)