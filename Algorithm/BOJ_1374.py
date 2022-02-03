import sys
from heapq import heappop, heappush
input = sys.stdin.readline

start = []
end = []

for _ in range(int(input())):
  n, a, b = map(int,input().split())
  start.append((a,b))

for a, b in sorted(start):
  if end:
    c = heappop(end)
    if a < c:
      heappush(end, c)
  heappush(end, b)

print(len(end))