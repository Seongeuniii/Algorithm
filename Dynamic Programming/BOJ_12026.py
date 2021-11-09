N = int(input())
cmd = input()
dp = [0]*N
for i in range(N):
  if dp[i] == 0 and i != 0:
    continue
  if cmd[i] == 'B': find = 'O'
  elif cmd[i] =='O': find = 'J'
  else: find = 'B'
  for j in range(i+1,N):
    if cmd[j] == find:
      if dp[j] == 0:
        dp[j] = dp[i]+(i-j)**2
      else:
        dp[j] = min(dp[j],dp[i]+(i-j)**2)
if dp[-1] != 0 or N == 1:
  print(dp[-1])
else:
  print(-1)