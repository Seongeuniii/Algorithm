import sys
N = int(sys.stdin.readline())
li = [0]
li.extend(list(map(int,sys.stdin.readline().split())))
if N == 1:
    print(li[1])
    sys.exit()
dp = [0 for _ in range(N+1)]
for i in range(1,N+1):
    dp[i] = li[i]
    for j in range(i-1,0,-1):
        dp[i] = max(dp[i],dp[j]+dp[i-j])
print(dp[N])