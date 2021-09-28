import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(10001)]
dp[1] = 1
def fibonacci(n):
    dp[n] = dp[n-1] + dp[n-2]
for i in range(2,n+1):
    fibonacci(i)
print(dp[n])