import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(1001)]
li = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    dp[li[i]] = max(dp[:li[i]]) + li[i]
print(max(dp))