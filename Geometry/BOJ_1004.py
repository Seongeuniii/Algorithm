import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  result = 0
  sx, sy, ex, ey = map(int,input().split())
  n = int(input())
  for _ in range(n):
    cnt = 0 
    hx, hy, r = map(int,input().split())
    if (sx-hx)**2 + (sy-hy)**2 > r**2:
      cnt += 1
    if (ex-hx)**2 + (ey-hy)**2 > r**2:
      cnt += 1
    if cnt == 1:
      result += 1
  print(result)