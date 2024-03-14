import sys
input = sys.stdin.readline

def dfs(x, y):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    max_v = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < N and ny >=0 and ny < N:
            if board[nx][ny] <= board[x][y]: continue

            v = dfs(nx, ny) if not dp[nx][ny] else dp[nx][ny]
            if v > max_v:
                max_v = v

    dp[x][y] = max_v + 1
    return dp[x][y]

board = []
bamboo = []

N = int(input())
for n in range(N):
    board.append(list(map(int, input().split())))
    for m in range(N):
        bamboo.append((board[n][m], n, m))

dp = [[0] * N for _ in range(N)]
for v, n, m in sorted(bamboo, reverse=True):
    dp[n][m] = dfs(n, m)

answer = 0
for n in range(N):
    answer = max(answer, max(dp[n]))

print(answer)
