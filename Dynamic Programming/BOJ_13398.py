N = int(input())
li = list(map(int,input().split()))

n_d = [0]*N
d = [0]*N
n_d[0] = li[0]

for i in range(1,N):
  if n_d[i-1] + li[i] > li[i]:
    n_d[i] = n_d[i-1] + li[i]
  else:
    n_d[i] = li[i]

  d[i] = max(n_d[i-1], d[i-1] + li[i])

print(max(n_d + d[1:]))