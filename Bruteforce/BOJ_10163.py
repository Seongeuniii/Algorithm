import sys
input = sys.stdin.readline

def solution():
  N = int(input())
  answer = [0]*(N+1)
  board = [[0]*1001 for _ in range(1001)]

  for i in range(1, N+1):
    [x, y, w, h] = list(map(int,input().split()))
    for a in range(x, x+w):
      for b in range(y, y+h):
        board[a][b] = i
  
  for i in range(1001):
    for j in range(1001):
      answer[board[i][j]] += 1

  for i in range(1, N+1):
    print(answer[i])

solution()