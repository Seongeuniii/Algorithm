import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
  serial = input().strip()
  s_sum = 0
  for s in serial:
    try:
      s_sum += int(s)
    except:
      continue

  heappush(heap, (len(serial), s_sum, serial))

for i in range(N):
  a,b,c = heappop(heap)
  print(c)
