def dfs(e, v):
  global answer 

  if len(e) == 3:
    answer = max(answer, v + e[0]*e[-1])
    return

  for i in range(1, len(e)-1):
    dfs(e[:i]+e[i+1:], v + e[i-1] * e[i+1])

N = int(input())
answer = 0
dfs(list(map(int, input().split())), 0)
print(answer)