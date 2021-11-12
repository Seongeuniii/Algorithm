num = input()
dp = [0]*41
dp[0] = 1
dp[1] = 1
for i in range(2,len(num)+1):
  if num[i-1] != '0':
    dp[i] += dp[i-1]
  if num[i-2] != '0' and 0 < int(num[i-2]+num[i-1]) < 35:
    dp[i] += dp[i-2]
print(dp[len(num)])