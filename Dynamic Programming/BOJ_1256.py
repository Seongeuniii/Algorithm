import sys
n = int(sys.stdin.readline())
li,dp = [0 for _ in range(10001)], [0 for _ in range(10001)]
for k in range(1,n+1):
    li[k] = int(sys.stdin.readline())
dp[1],dp[2] = li[1], li[1]+li[2]
for i in range(3,n+1):
    dp[i] = max(dp[i-1],dp[i-2]+li[i],dp[i-3]+li[i-1]+li[i])
print(dp[n])