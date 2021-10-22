N = int(input())
num = list(map(int,input().split()))
M = int(input())
dp = [-1 for _ in range(M+1)]
dp[M] = ''
for i in range(1,N):
  cnt = 1
  value = num[i]*cnt
  while M-value >= 0:
    for j in range(value,M+1):
      if dp[j] == -1 :
        continue
      newnum = str(i)*cnt + dp[j]
      newchange = j-value
      if dp[newchange] == '':
        dp[newchange] = newnum
      else:
        if int(newnum) > int(dp[newchange]):
          dp[newchange] = newnum
    cnt += 1
    value = num[i]*cnt
result = 0

for k in range(M):
  if dp[k]==-1 or dp[k]=='':
    continue
  zero = '0' * (k//num[0])
  result = max(int(dp[k]+zero),result)
print(result)