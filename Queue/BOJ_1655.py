import sys
from heapq import heappop,heappush
input = sys.stdin.readline

N = int(input())
MAX_HEAP = []
MIN_HEAP = []

std = int(input())
print(std)

for i in range(2,N+1):
  x = int(input())
  if len(MAX_HEAP) == len(MIN_HEAP):
    if x >= std:
      heappush(MIN_HEAP,x)
      print(std)
    else:
      heappush(MIN_HEAP,std)
      heappush(MAX_HEAP,-x)
      std = -heappop(MAX_HEAP)
      print(std)
  else: # len(MAX_HEAP) < len(MIN_HEAP)
    if x >= std:
      heappush(MAX_HEAP,-std)
      heappush(MIN_HEAP,x)
      std = heappop(MIN_HEAP)
      print(std)
    else:
      heappush(MAX_HEAP,-x)
      print(std)