import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for m in range(M): dp[0][m] = board[0][m]
for n in range(N): dp[n][0] = board[n][0]

answer = 0
for n in range(N):
    if n != 0:
        for m in range(1, M):
            if board[n][m]:
                dp[n][m] = min(dp[n - 1][m], dp[n][m - 1], dp[n - 1][m - 1]) + 1
    answer = max(answer, max(dp[n]))
print(answer**2)