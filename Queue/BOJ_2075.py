import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
  line = list(map(int,input().split()))
  li.extend(line)
  li.sort(reverse=True)
  li = li[:N]
print(li[-1])

# 큐
import sys
from heapq import heappush,heappop,heapify
input = sys.stdin.readline

N = int(input())
heap = list(map(int,input().split()))
heapify(heap)

for _ in range(N-1):
  line = sorted(list(map(int,input().split())), reverse=True)
  
  for l in line:
    if heap[0] < l:
      heappop(heap)
      heappush(heap, l)
    else:
      break
    
print(heappop(heap))