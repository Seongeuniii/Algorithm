import sys,math
input = sys.stdin.readline
N = int(input())
M = int(input())

answer = [[math.inf]*N for _ in range(N)]
for m in range(M):
  a,b,c = map(int,input().split())
  answer[a-1][b-1] = min(c, answer[a-1][b-1])

for u in range(N):
  answer[u][u] = 0

for k in range(N):
  for i in range(N):
    for j in range(N):
      if answer[i][k] + answer[k][j] < answer[i][j]:
        answer[i][j] = answer[i][k] + answer[k][j]

for z in range(N):
  for x in range(N):
    if answer[z][x] == math.inf:
      answer[z][x] = 0
  print(' '.join(map(str,answer[z])))