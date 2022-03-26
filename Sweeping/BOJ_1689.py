import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
  s, e = map(int, input().split())
  heappush(lines, (s, e))

answer = []
heap = []

while lines:
  s, e = heappop(lines)
  heappush(heap, e)

  while heap:
    end = heappop(heap)
    if end > s:
      heappush(heap, end)
      break

  answer.append(len(heap))

print(max(answer))