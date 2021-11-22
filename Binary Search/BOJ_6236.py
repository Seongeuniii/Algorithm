import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pay = [int(input()) for _ in range(N)]

s = max(pay)
e = sum(pay)

while s <= e:
  mid = (s+e)//2
  money = mid
  cnt = 1

  for p in pay:
    if money >= p:
      money -= p
    else:
      cnt += 1
      money = mid
      money -= p
      
  if cnt > M:
    s = mid + 1  
  else:
    e = mid - 1

print(mid)