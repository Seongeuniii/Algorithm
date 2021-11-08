dp = [0]*101
dp[1] = 1
n,m = map(int,input().split())
for i in range(2,n+1):
  dp[i] = dp[i-1]*i
print(dp[n]//(dp[n-m]*dp[m]))