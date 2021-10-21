N, K = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
li.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True)
result = set()
rank = 1
for i in range(N):
  for j in range(1,4):
    if li[i-1][j] != li[i][j]:
      rank = i+1
      break
  if li[i][0] == K:
    print(rank)
    exit()