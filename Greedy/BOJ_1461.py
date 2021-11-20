N,M = map(int,input().split())
book = list(map(int,input().split()))
minus = []
plus = []

for i in range(N):
  if book[i] < 0:
    minus.append(book[i])
  else:
    plus.append(book[i])

minus.sort()
plus.sort(reverse = True)
result = []

def test(li):
  idx = 0
  while True:
    if idx < len(li):
      result.append(abs(li[idx]))
      idx = idx+M
    else:
      break

test(minus)
test(plus)
print(sum(result)*2-max(result))