N = int(input())
line = sorted([list(map(int,input().split())) for _ in range(N)])
dp = [[0,0]]*N
result = 0
for i in range(N):
  dp[i] = [line[i][1],1]
  for j in range(i):
    if line[i][1] > dp[j][0]:
      dp[i][1] = max(dp[i][1],(dp[j][1]+1))
      result = max(dp[i][1],result)
print(N-result)