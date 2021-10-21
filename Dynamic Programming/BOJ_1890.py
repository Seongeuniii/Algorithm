N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    
    if dp[i][j] == 0 or i==j==N-1:
      continue

    if i+board[i][j] < N:
      dp[i+board[i][j]][j] += dp[i][j]

    if j+board[i][j] < N:
      dp[i][j+board[i][j]] += dp[i][j]

print(dp[N-1][N-1])

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):

    idx = 1
    while j-idx >= 0:
      if board[i][j-idx] == idx:
        dp[i][j] += dp[i][j-idx]
      idx += 1

    idx = 1
    while i-idx >= 0:
      if board[i-idx][j] == idx:
        dp[i][j] += dp[i-idx][j]
      idx += 1
      
print(dp[N-1][N-1])