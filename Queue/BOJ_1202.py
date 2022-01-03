import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N,K = map(int,input().split())

jewel = []
for _ in range(N):
  heappush(jewel, tuple(map(int,input().split())))

BAG = [int(input()) for _ in range(K)]

test = []
answer = 0

for bag in sorted(BAG):
  while jewel:
    m,v = heappop(jewel)
    if m <= bag:
      heappush(test,-v)
    else:
      heappush(jewel,(m,v))
      break
  if test:
    answer += heappop(test)

print(-answer)