import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
meets = []

for _ in range(N):
  s, e = map(int, input().split())
  heappush(meets, (s, e))

answer = 0
process = []

while meets:
  s, e = heappop(meets)

  if not process:
    heappush(process, e)
    answer += 1
  else:
    end = heappop(process)
    if s < end:
      answer += 1
      heappush(process, end)
    heappush(process, e)

print(answer)