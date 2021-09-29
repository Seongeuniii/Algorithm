import sys, math
N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
dp = [math.inf for _ in range(N)]
dp[0] = 0
for i in range(N-1):
    step = li[i]
    for j in range(i,i+step+1):
        if j >= N:
            break
        dp[j] = min(dp[j],dp[i]+1)
if dp[N-1] == math.inf:
    print(-1)
else:
    print(dp[N-1])