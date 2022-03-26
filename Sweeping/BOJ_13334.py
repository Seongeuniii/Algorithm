import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
locs = []
for _ in range(N):
  a, b = map(int,input().split())
  if a > b:
    a, b = b, a
  heappush(locs, (b, a))
D = int(input())

answer = 0
heap = []

while locs:
  e, s = heappop(locs)
  heappush(heap, s)

  while heap:
    start = heappop(heap)

    if start >= e-D:
      heappush(heap, start)
      break
    
  answer = max(answer, len(heap))

print(answer)