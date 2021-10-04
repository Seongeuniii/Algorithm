import sys
N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
inc_dp = [1 for _ in range(N)]
dec_dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(0,i):
        if li[j] > li[i]:
            dec_dp[i] = max(dec_dp[i],dec_dp[j]+1)
for a in range(N-1,-1,-1):
    for b in range(a,N):
        if li[a] < li[b]:
            inc_dp[a] = max(inc_dp[a],inc_dp[b]+1)
result = 1
for k in range(N):
    result = max(result,inc_dp[k]+dec_dp[k])
print(result-1)