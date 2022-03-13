import sys
input = sys.stdin.readline

def solution():
  answer = 1

  for n in range(N):
    for m in range(M):
      for i in range(min(n,m), 0, -1):
        if board[n][m] == board[n-i][m-i] == board[n-i][m] == board[n][m-i]:
          answer = max(answer, (i+1)**2)
          break
  
  return answer

N, M = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(N)]

print(solution())