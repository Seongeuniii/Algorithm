N,M = map(int,input().split())
active_memory = [0] + list(map(int,input().split()))
active_cost = [0] + list(map(int,input().split()))
dp = [[0 for _ in range(100*N+1)] for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(100*N+1):
        memory = active_memory[i]
        cost = active_cost[i]

        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(memory + dp[i - 1][j - cost], dp[i - 1][j])
            
for c in range(100*N+1):
  if dp[N][c] >= M:
    print(c)
    break