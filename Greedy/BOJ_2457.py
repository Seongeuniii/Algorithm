import sys
from heapq import heappush, heappop
input = sys.stdin.readline
date = []
answer = 0

for _ in range(int(input())):
  heappush(date, tuple(map(int, input().split())))
  
a, b = 3, 1
heap = []

while True:
  while date:
    sa, sb, ea, eb = heappop(date)
    if sa < a or (sa == a and sb <= b):
      heappush(heap, (-ea, -eb))
    else:
      heappush(date, (sa, sb, ea, eb))
      break

  if not heap:
    print(0)
    break

  else:
    ea, eb = heappop(heap)
    if -ea > a or (-ea == a and -eb >= b):
      a, b = -ea, -eb
      answer += 1
      if a > 11 or (a == 11 and b > 30):
        print(answer)
        break
    else:
      print(0)
      break