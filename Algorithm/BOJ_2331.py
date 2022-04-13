A, P = map(int, input().split())

num = {A: 0}
answer = 0

idx = 0
while True:
  idx += 1
  nA = 0
  for i in str(A):
    nA += int(i)**P

  if nA in num.keys():
    answer = num[nA]
    break
  else:
    A = nA
    num[nA] = idx

print(answer)