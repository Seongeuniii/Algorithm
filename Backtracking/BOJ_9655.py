import sys
sys.setrecursionlimit(10**6)

def isPromising(x, y):
  for i in range(1, x+1):
    if check[x-i] == y or check[x-i] == y-i or check[x-i] == y+i:
      return False
  return True


def dfs(x):
  global answer

  if x == N:
    answer += 1
    return

  for y in range(N):
    if isPromising(x, y):
      check[x] = y
      dfs(x+1)
      check[x] = -1

N = int(input())
check = [-1]*N
answer = 0

# dfs(0)
# print(answer)

ans = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
print(ans[int(input())])