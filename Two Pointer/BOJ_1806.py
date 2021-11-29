N,S = map(int,input().split())
li = list(map(int,input().split()))

e = 0
answer = 100000
ism = 0

for s in range(N):
  while ism < S and e < N:
    ism += li[e]
    e += 1
  
  if ism >= S:
    answer = min(answer, e-s)

  ism -= li[s]

if answer == 100000:
  print(0)
else:
  print(answer)