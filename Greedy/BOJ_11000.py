import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
heap = []
endtime = []
for _ in range(N):
  a, b = map(int,input().split())
  heappush(heap, (a,b))

while heap:
  s, e = heappop(heap)
  if endtime:
    t = heappop(endtime)
    if s >= t:
      heappush(endtime, e)
    else:
      heappush(endtime, t)
      heappush(endtime, e)
  else:
    heappush(endtime, e)

print(len(endtime))