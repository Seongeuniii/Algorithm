dp = [1 for _ in range(1000001)]
dp[2] = 2
for i in range(3,1000001):
  dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009
T = int(input())
for _ in range(T):
  n = int(input())  
  print(dp[n])