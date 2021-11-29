def test(n):
  X = str(n)
  d = int(X[1])-int(X[0])
  for j in range(2,len(X)):
    if int(X[j])-int(X[j-1]) != d:
      return 0
  return 1

N = int(input())
cnt = 0
for i in range(1,N+1):
  if 0<i<100:
    cnt += 1
  else:
    cnt += test(i)

print(cnt)

N = int(input())
cnt = 0

for i in range(1,N+1):
  if i < 100:
    cnt += 1
  else:
    num = list(map(int,str(i)))
    if num[0]-num[1] == num[1]-num[2]:
      cnt += 1

print(cnt)