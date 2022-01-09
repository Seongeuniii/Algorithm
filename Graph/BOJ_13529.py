import math
from heapq import heappop,heappush 

N,K = map(int,input().split())

loc_range = 100000
check = [math.inf]*(2*loc_range+1)

def dijkstra(start):
  heap = []
  heappush(heap,(0,start))
  check[start] = 0

  while heap:
    cnt, nd = heappop(heap)
    if 2*nd <= 2*loc_range and check[2*nd] > cnt:
      check[2*nd] = cnt
      heappush(heap, (cnt, 2*nd))
    if nd-1 >= 0 and check[nd-1] > cnt + 1:
      check[nd-1] = cnt + 1
      heappush(heap, (cnt+1, nd-1))
    if nd+1 <= 2*loc_range and check[nd+1] > cnt + 1:
      check[nd+1] = cnt + 1
      heappush(heap, (cnt+1, nd+1))

  return check[K]

print(dijkstra(N))